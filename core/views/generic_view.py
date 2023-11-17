# -*- coding: utf-8 -*-

#PRODUCCION

from functools import wraps
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from gestioncore.repository.generic_repository import GenericRepository
from gestioncore.utils.table_query import table_query
from django.core.mail import send_mail
from django.db import connection, transaction
import pyexcel as pe
import jwt
import json
import bcrypt
import logging
import time
from heyoo import WhatsApp
from urllib.parse import unquote
import requests
# from whatsapp_api_client_python import WhatsAppClient

import pandas as pd
from io import StringIO
import os
import subprocess
from decouple import config
import sys


generic_repository = GenericRepository()

sys.stdout.reconfigure(encoding='utf-8')

def clausula_query(table_query, entidad, setInputValues):
    entidad_info = next(
        (item for item in table_query if item["entidad"] == entidad), None
    )
    
    print('holamundo')

    if entidad_info:
        default_table = entidad_info["def"]
        
        print('setInputValues', setInputValues)
        print('entidad_info_1', entidad_info['query'])
        
        
        # entidad_info["query"] = entidad_info[f"query{setInputValues['query']}"]
        entidad_info["query"] = entidad_info[f"query{unquote(setInputValues['query'])}"]

        decoded_values = {key: unquote(value) for key, value in setInputValues.items()}
        
        
        for index, (campo0) in enumerate(entidad_info["params"]):
            found = False

            for name, value in decoded_values.items():
                if campo0 == name:
                    
                    # value = value.encode('utf-8').decode('utf-8')
                    # value = unquote(value)
                    entidad_info["query"] = entidad_info["query"].replace(name, str(value))
                    found = True
                    break
            if not found:
                entidad_info["query"] = entidad_info["query"].replace(
                    campo0, default_table[index]
                )
    print("entidad_info_2", entidad_info["query"])            
    return table_query



def with_entidad(metodo):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, entidad, *args, **kwargs):
            
            
            logger = logging.getLogger(__name__)
            
            # Dentro de tu vista
            logger.debug(request.data)

            
            entity_info = None
                
            print('entity', entity_info) 
            
            
            if "_p1" in request.data:
                try:
                    
                    decoded_p1 = unquote(request.data["_p1"])
                except Exception as e:
                    error_message = str(e)
                    print('Error:', error_message)
            #_p2,_p3 
            
            
            for query in table_query:
                if query["entidad"] == entidad:
                    entity_info = query
                    break
                

            if not entity_info:
                return Response(
                    {"error": "Entidad no encontrada"},
                    status=status.HTTP_404_NOT_FOUND,
                )
                
                
           
                
            if request.content_type == 'application/json':
                if "_p1" in request.data or "_p2" in request.data:
                    setInputValues = request.data
            else:
                setInputValues = request.query_params.dict()


            print('setInputValues', setInputValues)

            campos_busqueda = {
                campo: valor for campo, valor in setInputValues.items() if campo != "q"
            }
            
            
            clausula_query(table_query, entidad, campos_busqueda)   
            
            try:
                datos = metodo(
                    generic_repository,
                    entity_info.get("query")
                )
                return view_func(request, entidad, datos, *args, **kwargs)
            
            except Exception as e:
                print(e)
                error_message = str(e)
                return Response(
                    {"error": error_message},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return _wrapped_view

    return decorator


@api_view(["GET"])
@with_entidad(metodo=GenericRepository.listar)
def listar_view(request, entidad, datos):
    try:
        print('request', request.data)
        # encoded_data = json.dumps(datos, ensure_ascii=False).encode("utf-8")
        return JsonResponse(datos, status=status.HTTP_200_OK, safe=False,json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        error_message = str(e)
        print(error_message)
        return Response(
            {"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
     
@api_view(['POST'])
@with_entidad(metodo=GenericRepository.listar)
def crear(request, entidad, datos):
    try:
        print('datos', datos)
        return Response({"mensaje": "Creado correctamente", "datos":datos}, status= status.HTTP_200_OK)
    except Exception as e:
        error_message= str(e)
        return Response({"error:":error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

      
@api_view(['DELETE'])
@with_entidad(metodo=GenericRepository.editar)
def eliminar(request,entidad,error):
    try:
        return Response({"mensaje": "Eliminado correctamente"}, status= status.HTTP_200_OK)
    except Exception as e:
        error_message = str(e)
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
@with_entidad(metodo=GenericRepository.listar)
def editar(request,entidad,datos):
    try:
            # nombre_codificado = request.data.get('_p1', '')
            # nombre_decodificado = nombre_codificado.replace('+', ' ')
            # print('nombre_decodificado:', nombre_decodificado)
            return Response({"mensaje": "Edicion realizada exitosamente", "datos":datos})
    except Exception as e:
        error_message= str(e)
        return Response({"error:":error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(["GET"])
@with_entidad(metodo=GenericRepository.listar)
def exportar_a_excel_view(request, entidad, datos):
    try:
        encabezado = None

        for item in table_query:
            if item["entidad"] == entidad:
                encabezado = item["head"]
                break

       
        datos_unicode = [[str(item, 'utf-8') if isinstance(item, bytes) else str(item) for item in row] for row in datos]

        
        data = [encabezado] + datos_unicode

        book = pe.get_book(bookdict={entidad: data}, encoding="utf-8")
        xls_data = book.save_to_memory("xls")

    
        response = HttpResponse(xls_data.getvalue(), content_type="application/vnd.ms-excel")
        response["Content-Disposition"] = f'attachment; filename="{entidad}.xls"'
        response["Content-Encoding"] = "utf-8" 

        return response
    except Exception as e:
        error_message = str(e)
        print(error_message)
        return Response(
            {"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
@api_view(['GET'])
def sse(request):
    # Funci贸n que genera eventos SSE
    def event_stream():
        while True:
            time.sleep(3)  # Espera 3 segundos entre cada evento
            yield 'data: Estoy conectado\n\n'

    # Crea una respuesta HTTP en streaming con eventos SSE
    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['Connection'] = 'keep-alive'
    return response
    
    
#Cambiar base de datos a prod o dev    
@api_view(["POST"])
def cambiar_configuracion(request):
    try:
        eleccion = request.POST.get('eleccion')
    
        # if eleccion == 'produccion':
        #     os.environ['DB_ENVIROMENT'] = 'produccion'
        #     respuesta = {'mensaje': 'Configuracion cambiada a produccion'}
        # elif eleccion == 'desarrollo':
        #     os.environ['DB_ENVIROMENT'] = 'desarrollo'
        # else:
        #     respuesta = {"mensaje": "Eleccion no valida"}
        
        # subprocess.Popen(["sudo", "systemctl", "restart", "gunicorn.service"])
        # return Response(respuesta, status=status.HTTP_200_OK)
        # db_environment = os.environ.get('DB_ENVIRONMENT')
        
        if eleccion in ('production', 'development'):
            config('DB_ENVIRONMENT', eleccion)
            respuesta = {'mensaje': f'ConfiguraciOn cambiada a {eleccion}'}
        
            try:
                subprocess.run(['sudo', 'systemctl', 'restart', 'gunicorn.service'], check=True)
            except subprocess.CalledProcessError:
                respuesta['mensaje'] = 'Configuracion cambiada, pero ocurrio un error al reiniciar la aplicacion.'
        else:
            respuesta = {'mensaje': 'Eleccion no valida'}
        db_environment = config('DB_ENVIRONMENT')
        

        
        # print('db_environment',db_environment)
        return Response(respuesta, status= status.HTTP_200_OK)
    except:
        error_message = str(e)
        return Response ({"Error": error_message}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@api_view(["POST"])
@with_entidad(metodo=GenericRepository.listar)
def forgot_password(request, entidad, datos):
    try:
        user = {
            'id': datos[0][0],
        }
        recipient_email = datos[0][2]
        token = jwt.encode(user, 'clavesupersecreta', algorithm='HS512')
        token_seguro = token.replace('.', '@@@')
        send_mail(
            'Recuperar Password',
            f'Para recuperar password ingresa al siguiente link, https://gestionot.mtoopticos.cl/resetpassword/{token_seguro}',
            'admin@mtoopticos.cl',
            [recipient_email]
        )
        return Response({'mensaje': 'Correo Enviado', 'token_seguro': token_seguro}, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = str(e)
        print(error_message)
        return Response(
            {"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
      )
      

@api_view(["POST"])
def change_passwrod(request):
    try:
        data = request.data
        _p1 = data["_p1"]
        _p2 = data["_p2"]
        _p3 = data["_p3"]

        sql_query = [4, _p1 , _p2, _p3, 0, 0]

        print('query', sql_query)
        
        with connection.cursor() as cursor:
            cursor.callproc('spUsuarios', sql_query)
            cursor.close()  
            
        return Response({'Password actualizada'}, status=status.HTTP_200_OK) 
    except Exception as e:
        error_message = str(e)
        print(error_message)
        return Response({"Error": error_message},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


@api_view(['POST'])
def verify_password(request):
    try:
        password = request.data["password"]
        print('password', request.data)
        
        
        return Response({"mensaje": password}, status= status.HTTP_200_OK)
    except Exception as e:
        error_message= str(e)
        return Response({"error:":error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def types_excel(request):
    try:
        data = request.data
        table_name = data["table_name"]
        
        sql_query = f""" SELECT 
                           COLUMN_NAME, 
                           COLUMN_TYPE, 
                           IS_NULLABLE ,
                           CHARACTER_MAXIMUM_LENGTH AS longitud 
                        FROM information_schema.columns 
                        WHERE TABLE_NAME = '{table_name}'
                        AND TABLE_SCHEMA = "mtooptic_otprod"
                        ORDER BY ORDINAL_POSITION;
        """
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            resultUser = cursor.fetchall()
        
        resultUser_json = json.dumps(resultUser)
            
        return JsonResponse({"resul": resultUser_json}, status=status.HTTP_200_OK)

    except Exception as e:
        error_message = str(e)
        return Response({"error:":error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@transaction.atomic
def import_excel(request):
    try:
        excel_file = request.data['file']
        #df = pd.read_excel(excel_file,dtype={'CODIGO': str})
        df = pd.read_excel(excel_file)
        
        
        print('df antes', df)
        for column_name, column_data in df.items():
            print(f"Columna: {column_name}, Tipo de dato: {column_data.dtype}")
            
            if 'FECHA' in column_name:
                print('fechas', df[column_name])
            elif column_data.dtype == 'object':
                df[column_name].fillna(' ', inplace=True)
            elif pd.api.types.is_numeric_dtype(column_data):
                # Columna tipo número: reemplaza valores vacíos con 0
                df[column_name].fillna(0, inplace=True)
        
        print('df despues', df)
        
        positions_to_remove = request.data.get('positions_to_remove', 'undefined')
        print('positions_to_remove',positions_to_remove)
        
        if positions_to_remove != 'undefined':
            positions_to_remove = json.loads(positions_to_remove)
            df.drop(df.columns[positions_to_remove], axis=1, inplace=True)
        
        
        _table   = json.loads(request.data.get('entidad', '[]'))
        
        
        _data = df.values.tolist() 
        _fields = [col.lower() for col in df.columns]


        
        
        errors = []  # Arreglo para almacenar los errores
        
        
        # Iterar sobre los datos e intentar insertar cada fila
        with transaction.atomic():
            for row in _data:
                values_str = str(tuple(row))
                sql_query = f"""   
                    INSERT INTO {_table} ({', '.join(_fields)})
                    VALUES {values_str};
                """ 
                print('sql_query', sql_query)
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sql_query)
                except Exception as e:
                    transaction.set_rollback(True)
                    errors.append(str(e))
                    break;
        
        print(errors)
        
        if errors:
            return Response({"Errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"mensaje": "credo correctamente"}, status=status.HTTP_200_OK)
        
    except Exception as e:
        error_message = str(e)
        return Response({"Errror": error_message},status.HTTP_500_INTERNAL_SERVER_ERROR)
 

# @api_view(['POST'])
# @transaction.atomic
# def import_excel_ot(request):
#     try:
#         excel_file = request.data['file']
#         df = pd.read_excel(excel_file)
        
        
#         print('df antes', df)
#         for column_name, column_data in df.items():
#             print(f"Columna: {column_name}, Tipo de dato: {column_data.dtype}")
            
#             if 'FECHA' in column_name:
#                 print('fechas', df[column_name])
#             elif column_data.dtype == 'object':
#                 df[column_name].fillna(' ', inplace=True)
#             elif pd.api.types.is_numeric_dtype(column_data):
#                 # Columna tipo número: reemplaza valores vacíos con 0
#                 df[column_name].fillna(0, inplace=True)
        
        
        
#         _table   = json.loads(request.data.get('entidad', '[]'))
        
        
#         _data = df.values.tolist() 
#         _fields = [col.lower() for col in df.columns]
#         errors = [] 
        
        
        
#         with transaction.atomic():
#             for row in _data:
#                 values_str = str(tuple(row))
#                 sql_query = f"""   
#                     INSERT INTO {_table} ({', '.join(_fields)})
#                     VALUES {values_str};
#                 """ 
#                 print('sql_query', sql_query)
#                 try:
#                     with connection.cursor() as cursor:
#                         cursor.execute(sql_query)
#                 except Exception as e:
#                     transaction.set_rollback(True)
#                     errors.append(str(e))
#                     break;
        
#         print(errors) 
        
#         if errors:
#             return Response({"Errors": errors}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"mensaje": "credo correctamente"}, status=status.HTTP_200_OK)
        
#     except Exception as e:
#         error_message = str(e)
#         return Response({"Errror": error_message},status.HTTP_500_INTERNAL_SERVER_ERROR)
 
        

@api_view(["GET"])
def long_polling():
    try:
        # sql_query_cargos = "INSERT INTO Cargos (nombre) VALUES ('nueva OT')"
        # sql_query_cargos = "SELECT * FROM Cargos ORDER BY id DESC LIMIT 1;"
        
        # with connection.cursor() as cursor:
            # cursor.execute(sql_query_cargos)
            # resultcargos = cursor.fetchall()
         
        # print('cargo', resultcargos)
        
        # time.sleep(4)
            
  
        # sql_query_last_cargo = "SELECT * FROM Cargos ORDER BY id DESC LIMIT 1"   
         
        # with connection.cursor() as cursor:
        #     cursor.execute(sql_query_last_cargo)
        #     resultCargo = cursor.fetchone() 
            
        
        return JsonResponse({"data":'cargo creado'},status=status.HTTP_200_OK )
    except Exception as e:
        error_message = str(e)
        return Response({"Error": error_message},status.HTTP_500_INTERNAL_SERVER_ERROR)






@api_view(["GET"])
def whastapp(request):
    try:
        mensaje = "hola mundo"
        token = 'EAAJBpfeM57cBOwRSl7QUK95Cf4ZB2cBGWDzTeK3vo3o0ZBpuvFFQw4ZBdENzjrt4R1V2O815Oi5j8UV2ZA4bgg78nHYSs45c9UEAcBFNZBztklRL04Ebp5oD1mS7RM7EcJvzsB42YsWZBs77MJY4TocyGRCxX0RpBPrXk6rYRDZBEmmkyA0dZAHnbRRRkq0PT2bOEOhSP42yZBC6WZBDcvYrBJEcTwu0BlDmiL'
        telefonoEnviar= '+56949018251'
        idNumeroTelefono = '136257992907951'
        
        textoMensaje = 'hola prueba'
        
        mensajeWa=WhatsApp(token, idNumeroTelefono) 
        
        print('was',mensajeWa )
        
        mensajeWa.send_message(textoMensaje,telefonoEnviar)
         # URL de la API de Facebook
        # api_url = 'https://graph.facebook.com/{{Version}}/FROM_PHONE_NUMBER_ID/messages'
        
        # # Datos del mensaje en formato JSON
        # message_data = {
        #     "messaging_product": "whatsapp",
        #     "to": "56949018251",
        #     "type": "template",
        #     "template": {
        #         "name": "hello_world",
        #         "language": {
        #             "code": "en_US"
        #         }
        #     }
        # }
    

        # Enviamos el mensaje
        
        # Encabezados de la solicitud
        # headers = {
        #     'Authorization': 'Bearer ACCESS_TOKEN',
        #     'Content-Type': 'application/json'
        # }
    
        # Realizar la solicitud POST a la API de Facebook
        # response = requests.post(api_url, json=message_data, headers=headers)
        
        
        # WHATSAPP_ACCOUNT_ID = "156730780847621"
        # WHATSAPP_NUMBER_ID = "136257992907951"
        # phone_number = "+56963497946"
        # message= "mi querida abby, si llegas a recibir este mensaje me podrias avisar porfavor, graciaas"
        
        # client = WhatsAppClient(WHATSAPP_ACCOUNT_ID, WHATSAPP_NUMBER_ID)
        # client.send_message(phone_number, message)
        
        
        # if request.method == "GET":
        #     hub_verify_token = request.GET.get('hub.verify_token')
        #     if hub_verify_token == "HolaNovato":
        #         return request.GET.get("hub.challlenge")
        #     else:
        #         return "error de autenticacion"
                
        # data = request.get_json()
        
        # print('data',data)
        
        return Response({"mensaje": "mensaje enviado"}, status=status.HTTP_200_OK) 
    except Exception as e:
        error_message = str(e)
        return Response({"Error": error_message},status.HTTP_500_INTERNAL_SERVER_ERROR)    







@api_view(["POST"])
def login(request):
    try:

        data = request.data
        
        correo = data["correo"]
        password = data["password"]
         
        sql_query_usuarios = f"""SELECT 
                                U.password, 
                                U.nombre, 
                                U.correo, 
                                U.cargo, 
                                U.id, 
                                U.telefono, 
                                U.estado,
                                U.permisos_campos
                                FROM Usuarios U 
                                WHERE LOWER(U.correo) = LOWER('{correo}') 
                                AND U.estado = 1;""" 
        
        print('sql_query', sql_query_usuarios)
                    
        with connection.cursor() as cursor:
            cursor.execute(sql_query_usuarios)
            resultUser = cursor.fetchall()
  
            
        if len(resultUser) == 0:
            return Response({"Credenciales Incorrectas"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # print('password', password)
        # print('resultUser', resultUser[0][0])
        # print('user_id', resultUser[0][4])
    
        resulthash = check_password(password, resultUser[0][0])
        
        if not resulthash:
            return Response({"Credenciales Erroneas"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        user_id = resultUser[0][4]
        
        sql_query_permisos = f"""SELECT  
        	F.id 		  AS 'FUNCIONALIDAD_ID', 
        	F.descripcion AS 'FUNCIONALIDAD', 
            P.usuario  	  AS 'USUARIO_ID', 
            U.nombre   	  AS 'USUARIO', 
            P.permiso 	  AS 'PERMISO'
            FROM Funcionalidades F
            LEFT JOIN Permisos P
            ON P.funcionalidad = F.id
            AND P.usuario = {user_id}
            LEFT JOIN Usuarios U
            ON U.id = P.usuario
            ORDER BY F.id;""" 
    
        with connection.cursor() as cursor:
            cursor.execute(sql_query_permisos)
            resultPermisos = cursor.fetchall()
        
        
        
        if not resultPermisos:
            return Response({"No hay Permisos"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
        permisos_dict = {}

        for permiso in resultPermisos:
            id_opcion = permiso[0]
            opcion_nombre = permiso[1]
            id_usuario = permiso[2]
            nombre_usuario = permiso[3]
            permiso_tipo = permiso[4]
        
            
            if permiso_tipo is not None:
              
                permiso_data = {
                    "id_opcion": id_opcion,
                    "opcion_nombre":opcion_nombre,
                    "permiso_tipo": permiso_tipo,
                }
        
                
                if id_opcion in permisos_dict:
                    permisos_dict[id_opcion].append(permiso_data)
                else:
                    
                    permisos_dict[id_opcion] = [permiso_data]
        
        print('resultUser:', resultUser[0])
        
        user = {
                "id": resultUser[0][4],
                "nombre": resultUser[0][1],
                "correo": resultUser[0][2],
                "cargo": resultUser[0][3],
                "telefono": resultUser[0][5],
                "estado": resultUser[0][6],
                "permisos": permisos_dict,
                "permisos_campos": resultUser[0][7]
          }

   
        token = jwt.encode(user, 'clavesupersecreta', algorithm='HS512')
            
        
        return Response({token}, status=status.HTTP_200_OK) 
        # return Response({'login:'}, status=status.HTTP_200_OK) 
    except Exception as e:
        error_message = str(e)
        print(error_message)
        return Response({"Error": error_message},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
   





    
      
      
      
        
def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8') 


def check_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))
