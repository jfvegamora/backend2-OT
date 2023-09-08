from django.db import connection
from django.db import IntegrityError

class CustomIntegrityError(Exception):
    def __init__(self, message):
        super().__init__(message)



class GenericRepository:
    # Export method

    def listar(
        self,
        query,
    ):
        sql_query = f"{query}"
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
        return result
    
    
    def editar(
        self,
        query,
    ):
        try:
            sql_query = f"{query}"
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
        except IntegrityError as e:
            error_message = str(e)
            print('error_message', error_message)
            if "Cannot delete or update a parent row" in error_message:
                raise CustomIntegrityError("No se pudo eliminar: Integridad de datos.")
            elif "Duplicate entry" in error_message:
                raise CustomIntegrityError("No se pudo guardar: Entrada duplicada.")
        except Exception as e:
            error_message = str(e)
            if "The document is empty" in error_message:
                raise CustomIntegrityError("No hay registros.")
            raise Exception("Error: " + error_message + ".")
        
        