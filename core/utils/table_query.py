table_query = [
            # *********** O T *********** 
            # OT HISTORICA
            {
                "entidad": "othistorica",
                "query"  : [],
                "head"   : ['', 'FOLIO', 'MOTIVO', 'AREA_ID', 'AREA', 'ESTADO_ID', 'ESTADO', 'VALIDAR_PARAMETRIZACION_ID', 'VALIDAR_PARAMETRIZACION', 
                            'ESTADO_IMPRESION_ID', 'ESTADO_IMPRESION', 'PROYECTO_ID', 'PROYECTO', 
                            'ESTABLECIMIENTO_ID', 'ESTABLECIMIENTO', "ESTABLECIMIENTO_TIPO_ID", "ESTABLECIMIENTO_TIPO", 
                            'RUT', 'NOMBRE', 'TIPO', 'SEXO', 'FECHA_NACIMIENTO', 'DIRECCION', 'REGION_ID', 'REGION', 'PROVINCIA_ID', 'PROVINCIA', 
                            'COMUNA_ID', 'COMUNA', 'TELEFONO', 'CORREO', 'OFTALMOLOGO_ID', 'OFTALMOLOGO', 
                            'FECHA_ATENCION', 'FECHA_ENTREGA_TALLER', 'FECHA_DESPACHO', 'FECHA_ENTREGA_CLIENTE', 
                            'PUNTO_VENTA_ID', 'PUNTO_VENTA', 'NUMERO_RECETA', 'FECHA_RECETA', 'TIPO_ANTEOJO_ID', 'TIPO_ANTEOJO', 
                            'A1_OD_ESF', 'A1_OD_CIL', 'A1_OD_EJE', 'A1_OD_AD', 
                            'A1_OI_ESF', 'A1_OI_CIL', 'A1_OI_EJE', 'A1_OI_AD', 'A1_DP', 'A1_ALT', 'A1_GRUPO', 
                            'A2_OD_ESF', 'A2_OD_CIL', 'A2_OD_EJE', 
                            'A2_OI_ESF', 'A2_OI_CIL', 'A2_OI_EJE', 'A2_DP', 'A2_GRUPO', 
                            'A1_OPCION_VTA_ID', 'A1_OPCION_VTA', 'A1_ARMAZON_ID', 'A1_ARMAZON', 
                            'A2_OPCION_VTA_ID', 'A2_OPCION_VTA', 'A2_ARMAZON_ID', 'A2_ARMAZON', 
                            'A3_OPCION_VTA_ID', 'A3_OPCION_VTA', 'A3_ARMAZON_ID', 'A3_ARMAZON', 
                            'CR1_OPCION_VTA_ID', 'CR1_OPCION_VTA', 'CR1_MARCA_ID', 'CR1_MARCA', 'CR1_DISENO_ID', 'CR1_DISENO', 
                            'CR1_INDICE_ID', 'CR1_INDICE', 'CR1_MATERIAL_ID', 'CR1_MATERIAL', 'CR1_TRATAMIENTO_ID', 'CR1_TRATAMIENTO', 
                            'CR1_COLOR_ID', 'CR1_COLOR', 'CR1_DIAMETRO', 'CR1_OD',  'CR1_OI', 'CR1_TRAT_ADIC_ID', 'CR1_TRAT_ADIC',
                            'CR2_OPCION_VTA_ID', 'CR2_OPCION_VTA', 'CR2_MARCA_ID', 'CR2_MARCA', 'CR2_DISENO_ID', 'CR2_DISENO', 'CR2_INDICE_ID', 'CR2_INDICE', 
                            'CR2_MATERIAL_ID', 'CR2_MATERIAL', 'CR2_TRATAMIENTO_ID', 'CR2_TRATAMIENTO', 
                            'CR2_COLOR_ID', 'CR2_COLOR', 'CR2_DIAMETRO', 'CR2_OD',  'CR2_OI', 'CR2_TRAT_ADIC_ID', 'CR2_TRAT_ADIC',
                            'MOTIVO_GTIA_ID', 'MOTIVO_GTIA', 'FOLIO_ASOCIADO', 'RESOLUCION_GTIA_ID', 'RESOLUCION_GTIA', 
                            'WORKTRACKING', 'NOTA_VENTA', 'NUMERO_FACTURA', 'FOLIO_INTERNO_MANDANTE', 'OBSERVACIONES'],
                "params" : ['_p1', '_p2', '_folio', '_rut', '_nombre', '_fecha_desde', '_fecha_hasta', '_proyecto', '_establecimiento', '_motivo', '_estado', '_usuario', "_id"],
                "def"    : ['','0','0','','','','','0','0','0','0','0','0'],
                "query01": "CALL spOTHistorica(1 , '_p1' , _p2 , _folio, '_rut', '_nombre', '_fecha_desde' ,'_fecha_hasta' ,_proyecto,_establecimiento,_motivo,_estado,_usuario,_id,0)",
                "query03": "CALL spOTHistorica(3, \"_p1\", 0, _folio, '', '', '', '', 0, 0, 0, 0,_usuario, 0 , 0)",
            },
            # OT DIARIA
            {
                "entidad": "ot",
                "query"  : [],
                "head"   : ['', 'FOLIO', 'MOTIVO', 'AREA_ID', 'AREA', 'ESTADO_ID', 'ESTADO', 'VALIDAR_PARAMETRIZACION_ID', 'VALIDAR_PARAMETRIZACION', 
                            'ESTADO_IMPRESION_ID', 'ESTADO_IMPRESION', 'PROYECTO_ID', 'PROYECTO', 
                            'ESTABLECIMIENTO_ID', 'ESTABLECIMIENTO', "ESTABLECIMIENTO_TIPO_ID", "ESTABLECIMIENTO_TIPO", 
                            'RUT', 'NOMBRE', 'TIPO', 'SEXO', 'FECHA_NACIMIENTO', 'DIRECCION', 'REGION_ID', 'REGION', 'PROVINCIA_ID', 'PROVINCIA', 
                            'COMUNA_ID', 'COMUNA', 'TELEFONO', 'CORREO', 'OFTALMOLOGO_ID', 'OFTALMOLOGO', 
                            'FECHA_ATENCION', 'FECHA_ENTREGA_TALLER', 'FECHA_DESPACHO', 'FECHA_ENTREGA_CLIENTE', 
                            'PUNTO_VENTA_ID', 'PUNTO_VENTA', 'NUMERO_RECETA', 'FECHA_RECETA', 'TIPO_ANTEOJO_ID', 'TIPO_ANTEOJO', 
                            'A1_OD_ESF', 'A1_OD_CIL', 'A1_OD_EJE', 'A1_OD_AD', 
                            'A1_OI_ESF', 'A1_OI_CIL', 'A1_OI_EJE', 'A1_OI_AD', 'A1_DP', 'A1_ALT', 'A1_GRUPO', 
                            'A2_OD_ESF', 'A2_OD_CIL', 'A2_OD_EJE', 
                            'A2_OI_ESF', 'A2_OI_CIL', 'A2_OI_EJE', 'A2_DP', 'A2_GRUPO', 
                            'A1_OPCION_VTA_ID', 'A1_OPCION_VTA', 'A1_ARMAZON_ID', 'A1_ARMAZON', 
                            'A2_OPCION_VTA_ID', 'A2_OPCION_VTA', 'A2_ARMAZON_ID', 'A2_ARMAZON', 
                            'A3_OPCION_VTA_ID', 'A3_OPCION_VTA', 'A3_ARMAZON_ID', 'A3_ARMAZON', 
                            'CR1_OPCION_VTA_ID', 'CR1_OPCION_VTA', 'CR1_MARCA_ID', 'CR1_MARCA', 'CR1_DISENO_ID', 'CR1_DISENO', 
                            'CR1_INDICE_ID', 'CR1_INDICE', 'CR1_MATERIAL_ID', 'CR1_MATERIAL', 'CR1_TRATAMIENTO_ID', 'CR1_TRATAMIENTO', 
                            'CR1_COLOR_ID', 'CR1_COLOR', 'CR1_DIAMETRO', 'CR1_OD',  'CR1_OI', 'CR1_TRAT_ADIC_ID', 'CR1_TRAT_ADIC',
                            'CR2_OPCION_VTA_ID', 'CR2_OPCION_VTA', 'CR2_MARCA_ID', 'CR2_MARCA', 'CR2_DISENO_ID', 'CR2_DISENO', 'CR2_INDICE_ID', 'CR2_INDICE', 
                            'CR2_MATERIAL_ID', 'CR2_MATERIAL', 'CR2_TRATAMIENTO_ID', 'CR2_TRATAMIENTO', 
                            'CR2_COLOR_ID', 'CR2_COLOR', 'CR2_DIAMETRO', 'CR2_OD',  'CR2_OI', 'CR2_TRAT_ADIC_ID', 'CR2_TRAT_ADIC',
                            'MOTIVO_GTIA_ID', 'MOTIVO_GTIA', 'FOLIO_ASOCIADO', 'RESOLUCION_GTIA_ID', 'RESOLUCION_GTIA', 
                            'WORKTRACKING', 'NOTA_VENTA', 'NUMERO_FACTURA', 'FOLIO_INTERNO_MANDANTE', 'OBSERVACIONES'],
                "params" :               ['_p1', '_p2', '_p3', '_folio', '_rut', '_fecha_desde', '_fecha_hasta', '_proyecto', '_establecimiento', '_origen', '_destino', '_estado', '_usuario', '_situacion', '_obs',   '_cristalesJSON'  ,    '_armazonesJSON'   ,  '_punto_venta' ,'_id'],
                "def"    :               [  '' ,  '0' ,   '' ,    '0'  ,   ''  ,       ''      ,       ''      ,      ''    ,        '0'        ,     '0'  ,     '0'   ,     '0'  ,     '0'   ,      '0'    ,   ''  ,      '\"\"'         ,      '\"\"'           ,      '0'        ,'0' ],
                "query01": "CALL spOT(1 ,   '' ,   0  ,   '' ,  _folio ,   ''  , '_fecha_desde', '_fecha_hasta', '_proyecto',  _establecimiento ,  _origen ,      0    ,      0   ,      0    ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         ,_id ,  0)",
                "query03": "CALL spOT(3,  '_p1',   0 ,  '_p3',     0   , '_rut',       ''      ,       ''      , '_proyecto',  _establecimiento ,  _origen ,  _destino ,  _estado ,  _usuario ,       0     ,   ''  ,   '_cristalesJSON'  ,    '_armazonesJSON'   , '_punto_venta'  , 0  ,  0)",
                "query04": "CALL spOT(4,  '_p1',   0 ,  '_p3',  _folio , '_rut',       ''      ,       ''      , '_proyecto',         0         ,  _origen ,  _destino ,  _estado ,  _usuario ,  _situacion , '_obs',   '_cristalesJSON'  ,    '_armazonesJSON'   , '_punto_venta'  , 0  ,  0)",
                "query05": "CALL spOT(5,    '' ,   0 ,    '' ,  _folio ,   ''  ,       ''      ,       ''      ,      ''    ,         0         ,  _origen ,  _destino ,  _estado ,  _usuario ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
                "query06": "CALL spOT(6,    '' , _p2 ,    '' ,  _folio ,   ''  ,       ''      ,       ''      ,      ''    ,         0         ,  _origen ,      0    ,  _estado ,  _usuario ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
                "query07": "CALL spOT(7,    '' , _p2 ,    '' ,  _folio ,   ''  ,       ''      ,       ''      ,      ''    ,         0         ,  _origen ,      0    ,  _estado ,  _usuario ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
                "query08": "CALL spOT(8,    '' , _p2 ,    '' ,  _folio ,   ''  ,       ''      ,       ''      ,      ''    ,         0         ,  _origen ,      0    ,  _estado ,  _usuario ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
                "query09": "CALL spOT(9,    '' , _p2 ,    '' ,  _folio ,   ''  ,       ''      ,       ''      ,      ''    ,         0         ,  _origen ,      0    ,  _estado ,  _usuario ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
                "query10": "CALL spOT(10,   '' , _p2 ,    '' ,  _folio ,   ''  ,       ''      ,       ''      ,      ''    ,         0         ,  _origen ,      0    ,  _estado ,  _usuario ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
                "query11": "CALL spOT(11,   '' ,   0 ,    '' ,       0 ,   ''  , '_fecha_desde',       ''      , '_proyecto',         0         ,        0 ,      0    ,        0 ,         0 ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
                "query12": "CALL spOT(12,   '' ,   0 , '_p3' ,       0 ,   ''  ,       ''      ,       ''      , '_proyecto',         0         ,        0 ,      0    ,        0 ,         0 ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
                "query13": "CALL spOT(13,   '' ,   0 ,    '' ,       0 , '_rut',       ''      ,       ''      ,      ''    ,         0         ,        0 ,      0    ,        0 ,         0 ,       0     ,   ''  ,      '\"\"'         ,      '\"\"'           ,       0         , 0  ,  0)",
            },
            # OTAREAS
            {
                "entidad": "otareas",
                "query"  : [],
                "head"   : [""],
                "params": ["_p1","_p2", "_id"],
                "def": ["", "0", "0"],
                "query01": "CALL spOTAreas(1, '', _p2 , 0, 0)",
            },
            # OTBITACORA
            {
                "entidad": "otbitacora",
                "query"  : [],
                "head"   : [""],
                "params": ["_p1","_p2", "_id"],
                "def": ["", "0", "0"],
                "query01": "CALL spOTBitacora(1, '', _p2 , 0, 0)",
                "query02": "CALL spOTBitacora(3, '', 0, 0, 0)",
            },

            # CLIENTES
            {
                "entidad": "clientes",
                "query"  : [],
                "head"   : ["", 'RUT', 'NOMBRE', 'TIPO', 'SEXO', 'FECHA_NACIMIENTO', 'DIRECCION', 
                            'REGION_ID', 'REGION', 'PROVINCIA_ID', 'PROVINCIA', 'COMUNA_ID', 'COMUNA',  
                            'TELEFONO', 'CORREO', 'ESTABLECIMIENTO_ID', 'ESTABLECIMIENTO'],
                "params" : ["_p1", "_p2", "_p3", '_pkToDelete', "_id"],
                "def"    : ["", "", "0", "", "0"],
                "query01": "CALL spClientes(1, '_p1', '_p2', _p3, '\"\"', _id, 0)",
                "query02": "CALL spClientes(2, '', '', 0, '\"\"', 0, 0)",
                "query03": "CALL spClientes(3, '_p1', '', 0, '\"\"', 0, 0)",
                "query04": "CALL spClientes(4, '_p1', _p2, 0, '\"\"', 0, 0)",
                "query05": "CALL spClientes(5, \"_p1\", '', 0, '\"\"', 0, 0)",
            },
            # ESTABLECIMIENTOS
            {
                "entidad": "establecimientos",
                "query"  : [],
                "head"   : ["", "ID", "CODIGO", "NOMBRE", "ESTABLECIMIENTO_TIPO_ID", "ESTABLECIMIENTO_TIPO", 
                            "MANDANTE", "MANDANTE_ID", "REGION_ID", "REGION", "PROVINCIA_ID", "PROVINCIA", "COMUNA_ID", "COMUNA"],
                "params" : ["_p1", "_p2", "_p3", "_id"],
                "def"    : ["", "0", "0", "0"],
                "query01": "CALL spEstablecimientos(1, '_p1', _p2, _p3, _id, 0)",
                "query02": "CALL spEstablecimientos(2,    '',   0,   0, 0, 0)",
                "query03": "CALL spEstablecimientos(3, '_p1',   0,   0, 0, 0)",
                "query04": "CALL spEstablecimientos(4, '_p1', _p2,   0, 0, 0)",
                "query05": "CALL spEstablecimientos(5, '_p1',   0,   0, 0, 0)",
                "query06": "CALL spEstablecimientos(6, '_p1',   0,   0, 0, 0)",
            },
            # PUNTOS DE VENTA
            {
                "entidad": "puntosventa",
                "query"  : [],
                "head"   : ["", 'ID', 'DESCRIPCION', 'TIPO_ID', 'TIPO', 'DIRECCION', 'TELEFONO', 
                        'ENCARGADO_ID', 'ENCARGADO', 'ALMACEN_ID', 'ALMACEN'],
                "params" : ["_p1", "_p2", "_id"],
                "def"    : ["", "0", "0"],
                "query01": "CALL spPuntosVenta(1, '_p1', '_p2', _id, 0)",
                "query02": "CALL spPuntosVenta(2,   '' , 0, 0, 0)",
                "query03": "CALL spPuntosVenta(3, '_p1', 0, 0, 0)",
                "query04": "CALL spPuntosVenta(4, '_p1', _p2, 0, 0)",
                "query05": "CALL spPuntosVenta(5, '_p1', 0, 0, 0)",
            },
            # SITUACIONES
            {
                "entidad": "otsituaciones",
                "query"  : [],
                "head"   : ["","ID", "SITUACIÓN", "AREA_ID", "AREA"],
                "params" : ["_p1", "_p2",'_id'],
                "def"    : ["", "0","0"],
                "query01": "CALL spSituaciones(1, '_p1', _p2,_id, 0)",
                "query02": "CALL spSituaciones(2,   '' , _p2, 0, 0)",
                "query03": "CALL spSituaciones(3, '_p1', 0, 0, 0)",
                "query04": "CALL spSituaciones(4, '_p1', _p2, 0, 0)",
                "query05": "CALL spSituaciones(5, '_p1', 0, 0, 0)",
            },
            
            # *********** B O D E G A *********** 
            # ARMAZONES
            {
                "entidad": "armazones",
                "query": [],
                "head": ["", 'CODIGO', 'ARMAZON_TIPO_ID', 'ARMAZON_TIPO', 'MARCA_ID', 'MARCA', 'MODELO', 'COLOR', 
                        'ARMAZON_MATERIAL_ID', 'ARMAZON_MATERIAL', 'ARO', 'PUENTE', 'DIAGONAL', 'BRAZO', 
                        'ARMAZON_USO_ID', 'ARMAZON_USO', 'INGRESOS', 'EGRESOS', 
                        'STOCK_ACTUAL', 'STOCK_MINIMO', 'STOCK_RESERVADO', 'STOCK_DISPONIBLE'],
                "params": ["_p1", "_p2", "_p3", "_p4", "_id"],
                "def": ["", "", "0", "0", "0"],
                "query01": "CALL spArmazones(1,   '_p1', '_p2', _p3, _p4, _id, 100)",
                "query02": "CALL spArmazones(2,      '',   '' , 0, 0, 0, 0)",
                "query03": "CALL spArmazones(3,   '_p1',   '' , 0, 0, 0, 0)",
                "query04": "CALL spArmazones(4,   '_p1', '_p2', 0, 0, 0, 0)",
                "query05": "CALL spArmazones(5, \"_p1\",   '' , 0, 0, 0, 0)",
            },
            # ARMAZONES KARDEX
            {
                "entidad": "armazoneskardex",
                "query"  : [],
                "head"   : ["", 'FECHA', 'ARMAZON', 'DESCRIPCION', 'ALMACEN_ID', 'ALMACEN', 'ES', 'MOTIVO_ID', 'MOTIVO', 
                            'ENTRADAS', 'SALIDAS', 'VALOR_NETO', 'PROVEEDOR_ID', 'PROVEEDOR', 'FACTURA', 'OT', 
                            'ALMACEN_RELACIONADO_ID', 'ALMACEN_RELACIONADO', 'OBSERVACIONES', 'USUARIO_ID', 'USUARIO', 'FECHA_MOV'],
                "params" : ["_p1", "_p2", "_p3", "_p4", "_pkToDelete", "_id"],
                "def"    : ['0', '', '', '0', '\"\"', '0'],
                "query01": "CALL spArmazonesKardex(1, '_p1', '_p2', '_p3', _p4, '\"\"' , _id, 0);",
                "query03": "CALL spArmazonesKardex(3, '_p1',   '' ,   '' ,  0 , '_pkToDelete', 0, 0);",
                "query04": "CALL spArmazonesKardex(4, '_p1', '_p2', '_p3',  0 , '\"\"', 0, 0);",
                "query05": "CALL spArmazonesKardex(5, ''   ,   '' ,   '' ,  0 ,   '_pkToDelete', 0, 0);",
            },
            # CRISTALES
            {
                "entidad": "cristales",
                "query"  : [],
                "head"   : ["", 'CODIGO', 'MARCA_ID', 'MARCA', 'PROVEEDOR_ID', 'PROVEEDOR', 'DISENO_ID', 'DISENO',
                            'INDICE_ID', 'INDICE', 'MATERIAL_ID', 'MATERIAL', 'COLOR_ID', 'COLOR',
                            'TRATAMIENTO_ID', 'TRATAMIENTO', 'DIAMETRO', 'ESFERICO', 'CILINDRICO', 
                            'INGRESOS', 'EGRESOS', 'STOCK_ACTUAL', 'STOCK_MINIMO', 'STOCK_RESERVADO', 'STOCK_DISPONIBLE'],
                "params" : ["_p1", "_p2", "_pMarca","_pProveedor","_pDiseno", "_pIndice","_pMaterial", 
                            "_pColor", "_pTratamiento","_pDiametro", "_pEsferico","_pCilindrico", "_p4", "_id"],
                "def"    : ["0", "", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                "query01": "CALL spCristales(1, '_p1'  , '' , _pMarca, _pProveedor, _pDiseno, _pIndice, _pMaterial, _pColor, _pTratamiento, _pDiametro, _pEsferico, _pCilindrico, _p4, _id, 100);",
                "query02": "CALL spCristales(2, ''     , '' , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);", 
                "query03": "CALL spCristales(3, '_p1', '' , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
                "query04": "CALL spCristales(4, '_p1', _p2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
                "query05": "CALL spCristales(5, '_p1'  , 0  , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
                "query06": "CALL spCristales(5, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, _id, 0, 0);",
            },
            # CRISTALES KARDEX
            {
                "entidad": "cristaleskardex",
                "query"  : [],
                "head"   : ["", 'FECHA', 'CRISTAL', 'DESCRIPCION', 'ALMACEN_ID', 'ALMACEN', 'ES', 'MOTIVO_ID', 'MOTIVO', 
                            'ENTRADAS', 'SALIDAS', 'VALOR_NETO', 'PROVEEDOR_ID', 'PROVEEDOR', 'FACTURA', 'OT', 
                            'ALMACEN_RELACIONADO_ID', 'ALMACEN_RELACIONADO', 'OBSERVACIONES', 'USUARIO_ID', 'USUARIO', 'FECHA_MOV'],
                "params" : ["_p1", "_p2", "_p3", "_p4", "_pkToDelete", "_id"],
                "def"    : ['0', '', '', '0', '\"\"', '0'],
                "query01": "CALL spCristalesKardex(1, '_p1', '_p2', '_p3', _p4, '\"\"', _id, 0);",
                "query03": "CALL spCristalesKardex(3, '_p1',   '' ,   '' ,  0 , '\"\"', 0, 0);",
                "query04": "CALL spCristalesKardex(4, '_p1', '_p2', '_p3',  0 , '\"\"', 0, 0);",
                "query05": "CALL spCristalesKardex(5, ''  ,    '' ,   '' ,  0 , '_pkToDelete', 0, 0);",
            },
            # ACCESORIOS
            {
                "entidad": "accesorios",
                "query": [],
                "head": ["", "CODIGO", "DESCRIPCION", "MARCA_ID", "MARCA", "PROVEEDOR_ID", "PROVEEDOR", 
                         "PRECIO_NETO", 'INGRESOS', 'EGRESOS', 'STOCK_ACTUAL', "STOCK_MINIMO", 
                         'STOCK_RESERVADO', 'STOCK_DISPONIBLE'],
                "params": ["_p1", "_p2", "_p3", "_p4", "_id"],
                "def": ["", "", "0", "0", "0"],
                "query01": "CALL spAccesorios(1, '_p1', '_p2', _p3, _p4, _id, 100)",
                "query02": "CALL spAccesorios(2,   '' ,   '' ,  0 ,  0 , 0, 0)",
                "query03": "CALL spAccesorios(3, '_p1',   '' ,  0 ,  0 , 0, 0)",
                "query04": "CALL spAccesorios(4, '_p1',   0  , _p3,  0 , 0, 0)",
                "query05": "CALL spAccesorios(5, '_p1',   '' ,  0 ,  0 , 0, 0)",
            },
            # ACCESORIOS KARDEX
            {
                "entidad": "accesorioskardex",
                "query"  : [],
                "head"   : ["", 'FECHA', 'ACCESORIO', 'DESCRIPCION', 'ALMACEN_ID', 'ALMACEN', 'ES', 'MOTIVO_ID', 'MOTIVO', 
                            'ENTRADAS', 'SALIDAS', 'VALOR_NETO', 'PROVEEDOR_ID', 'PROVEEDOR', 'FACTURA', 'OT', 
                            'ALMACEN_RELACIONADO_ID', 'ALMACEN_RELACIONADO', 'OBSERVACIONES', 'USUARIO_ID', 'USUARIO', 'FECHA_MOV'],
                "params" : ["_p1", "_p2", "_p3", "_p4", "_pkToDelete", "_id"],
                "def"    : ['0', '', '', '0', '\"\"', '0'],
                "query01": "CALL spAccesoriosKardex(1, '_p1', '_p2', '_p3', _p4,  '\"\"', _id, 0);",
                "query03": "CALL spAccesoriosKardex(3, '_p1',   '' ,   '' ,  0 , '\"\"', 0, 0);",
                "query04": "CALL spAccesoriosKardex(4, '_p1', '_p2', '_p3',  0 , '\"\"', 0, 0);",
                "query05": "CALL spAccesoriosKardex(5,   '' ,   '' ,   '' ,  0 ,   '_pkToDelete', 0, 0);",
            },
            # PROVEEDORES
            {
                "entidad": "proveedores",
                "query": [],
                "head": ["", "ID", "RUT", "NOMBRE", "DIRECCION", "TELEFONO", "CORREO", "SITIO WEB"],
                "params": ["_p1", "_p2", "_p3","_id"],
                "def": ["", "0", "", "0"],
                "query01": "CALL spProveedores(1, '_p1', 0, '_p3', _id, 0)",
                "query02": "CALL spProveedores(2, '', 0,'', 0, 0)",
                "query03": "CALL spProveedores(3, '_p1', 0, '', 0, 0)",
                "query04": "CALL spProveedores(4, '_p1', _p2, '', 0, 0)",
                "query05": "CALL spProveedores(5, '_p1', 0, '', 0, 0)",
            },
            # ALMACENES
            {
                "entidad": "almacenes",
                "query"  : [],
                "head"   : ["", "ID", "DESCRIPCION", "TIPO_ALMACEN_ID", "TIPO_ALMACEN"],
                "params" : ["_p1", "_p2", "_id"],
                "def"    : ["", "0", "0"],
                "query01": "CALL spAlmacenes(1, '_p1', _p2, _id, 0)",
                "query02": "CALL spAlmacenes(2, '', 0, 0, 0)",
                "query03": "CALL spAlmacenes(3, '_p1', 0, 0, 0)",
                "query04": "CALL spAlmacenes(4, '_p1', _p2, 0, 0)",
                "query05": "CALL spAlmacenes(5, '_p1', 0, 0, 0)",
            },
            # MARCAS
            {
                "entidad": "marcas",
                "query": [],
                "head": ["", "ID", "NOMBRE", "PROVEEDOR_ID", "PROVEEDOR"],
                "params": ["_p1", "_p2", "_id"],
                "def": ["", "0", "0"],
                "query01": "CALL spMarcas(1, '_p1', _p2, _id, 0)",
                "query02": "CALL spMarcas(2, '', 0, 0, 0)",
                "query03": "CALL spMarcas(3, '_p1', 0, 0, 0)",
                "query04": "CALL spMarcas(4, '_p1', _p2, 0, 0)",
                "query05": "CALL spMarcas(5, '_p1', 0, 0, 0)",
            },

            # *********** P R O Y E C T O S *********** 
            # MANDANTES
            {
                "entidad": "mandantes",
                "query"  : [],
                "head"   : ["", "CODIGO", "RUT", "NOMBRE", "REGION_ID", "REGION", "PROVINCIA_ID", "PROVINCIA", "COMUNA_ID", "COMUNA"],
                "params" : ["_p1", "_p2", "_id"],
                "def"    : ["", "0", "0"],
                "query01": "CALL spMandantes(1, '_p1', _p2, _id, 0)",
                "query02": "CALL spMandantes(2, '', 0, 0, 0)",
                "query03": "CALL spMandantes(3, '_p1', 0, 0, 0)",
                "query04": "CALL spMandantes(4, '_p1', _p2, 0, 0)",
                "query05": "CALL spMandantes(5, '_p1', 0, 0, 0)",
            },
            # PROYECTOS
            {
                "entidad": "proyectos",
                "query"  : [],
                "head": ["","CODIGO", "CODIGO_LICITACION", "TÍTULO", "ESTADO",
                 "EMPRESA_ID", "EMPRESA", "MANDANTE_ID", "MANDANTE", "UNIDAD_COMPRA",
                 "FECHA_ADJUDICACION", "FECHA_INICIO", "FECHA_TERMINO", "CANTIDAD_REQUERIDA",
                 "PRESUPUESTO", "DIAS_DE_ENTREGA", "EJECUTIVO_ID","EJECUTIVO",
                 "CONTACTO_ADMINISTRADOR_NOMBRE", "CONTACTO_ADMINISTRADOR_CORREO", "CONTACTO_ADMINISTRADOR_TELEFONO", 
                 "REFERENTE_TECNICO_NOMBRE", "REFERENTE_TECNICO_CORREO","REFERENTE_TECNICO_TELEFONO", 
                 "CONTACTO_CONTABILIDAD_NOMBRE","CONTACTO_CONTABILIDAD_CORREO", "CONTACTO_CONTABILIDAD_TELEFONO",
                 "CONTACTO_FINANZAS_NOMBRE", "CONTACTO_FINANZAS_CORREO", "CONTACTO_FINANZAS_TELEFONO",
                 "OFTALMOLOGO_ID", "OFTALMOLOGO", "OBSERVACIONES"],
                "params" : ["_p1", "_p2", "_p3", "_p4", "_pkToDelete", "_id"],
                "def"    : [ '0' ,   '' ,   '' ,   '' ,     '\"\"'   ,  '0'],
                "query01": "CALL spProyectos(1, '_p1',  '_p2' , '_p3' , '_p4', '\"\"', _id, 0)",
                "query02": "CALL spProyectos(2,     0,  ''    ,    '' ,    '', '\"\"',   0, 0)",
                "query03": "CALL spProyectos(3,     0,  '_p2' ,    '' ,    '', '\"\"',   0, 0)",
                "query04": "CALL spProyectos(4,     0,  '_p2' , '_p3' ,    '', '\"\"',   0, 0)",
                "query05": "CALL spProyectos(5,     0, \"_p2\",    '' ,    '', '\"\"',   0, 0)",
            }, 
            # PROYECTO ARMAZONES
            {
                "entidad": "proyectoarmazones",
                "query": ['', 'PROYECTO', 'TITULO', 'LICITACION', 'CODIGO', 'PROVEEDOR_ID', 'PROVEEDOR', 
                          'TIPO_ID', 'TIPO', 'MARCA_ID', 'MARCA', 'MODELO', 'COLOR', 'MATERIAL_ID', 'MATERIAL', 
                          'ARO', 'PUENTE', 'DIAGONAL', 'BRAZO', 'USO_ID', 'USO', 'ESTADO'],
                "head": ["","", ""],
                "params": ["_p1", "_p2", '_p3', '_pkToDelete' ,'_id'],
                "def": ["", "", "", "","0"],
                "query01": "CALL spProyectoArmazones(1, '_p1', '_p2', '_p3','\"\"' ,_id, 0)",
                "query03": "CALL spProyectoArmazones(3, '_p1', '', '' , '\"\"' ,0, 0)",
                "query04": "CALL spProyectoArmazones(4, '_p1', \"_p2\", \"_p3\", '\"\"' , 0, 0)",
                "query05": "CALL spProyectoArmazones(5, '', '', '', '_pkToDelete'  ,0, 0)",
            },
            # PROYECTOS CRISTALES
            {
                "entidad": "proyectocristales",
                "query"  : [],
                "head": ["", 'PROYECTO','TITULO','LICITACION', 'GRUPO', 'DESCRIPCION', 'MARCA_ID', 'MARCA', 
                        'DISENO_ID', 'DISENO', 'INDICE_ID', 'INDICE', 'MATERIAL_ID', 'MATERIAL', 
                        'COLOR_ID', 'COLOR', 'TRATAMIENTO_ID', 'TRATAMIENTO',
                         'ESF_DESDE', 'CIL_DESDE', 'ESF_HASTA', 'CIL_HASTA', 'DIAMETRO', '$_VTA_NETO', 'OBSERVACIONES'],
                "params" : ["_p1", "_p2", '_p3', '_pkToDelete' ,'_id'],
                "def"    : ["", "", "", "\"\"", "0"],
                "query01": "CALL spProyectoCristales(1, '_p1'  , '_p2', '_p3', '\"\"', _id, 0)",
                "query02": "CALL spProyectoCristales(2, \"_p1\", ''   ,   0  , '\"\"', 0, 0)",
                "query03": "CALL spProyectoCristales(3, '_p1', 0, '', '\"\"', 0, 0)",
                "query04": "CALL spProyectoCristales(4, '_p1', \"_p2\",\"_p3\", '\"\"', 0, 0)",
                "query05": "CALL spProyectoCristales(5, '', '', '', '_pkToDelete', 0, 0)",
                "query06": "CALL spProyectoCristales(6, '', '_p2', '', '_pkToDelete', 0, 0)",
            }, 
            # PROYECTO ACCESORIOS
            {
                "entidad": "proyectosaccesorios",
                "query": [],
                "head": ['', 'PROYECTO', 'TITULO', 'LICITACION', 'ACCESORIO_ID', 'ACCESORIO', 'PROVEEDOR_ID', 'PROVEEDOR', 'MARCA_ID', 'MARCA', 'ESTADO'],
                "params": ["_p1", "_p2", '_p3', '_pkToDelete' ,'_id'],
                "def": ["", "","", "","0"],
                "query01": "CALL spProyectosAccesorios(1, '_p1', '_p2', '_p3','\"\"' ,_id, 0)",
                "query03": "CALL spProyectosAccesorios(3, '_p1', '', '' , '\"\"' ,0, 0)",
                "query04": "CALL spProyectosAccesorios(4, '_p1', \"_p2\",\"_p3\", '\"\"' , 0, 0)",
                "query05": "CALL spProyectosAccesorios(5, '', '', '', '_pkToDelete'  ,0, 0)",
            },
            # PROYECTOS DIRECCIONES DESPACHO
            {
                "entidad": "proyectodireccionesdespacho",
                "query"  : [],
                "head": ["", 'PROYECTO','TITULO','LICITACION','ESTABLECIMIENTO_ID','ESTABLECIMIENTO',
                         'LUGAR','DIRECCION', 'TELEFONO', 'OBSERVACIONES'],
                "params" : ["_p1", "_p2", '_p3', '_pkToDelete' ,'_id'],
                "def"    : ["", "", "", "\"\"", "0"],
                "query01": "CALL spProyectosDirecciones(1, '_p1', '_p2', '_p3', '\"\"', _id, 0)",
                "query03": "CALL spProyectosDirecciones(3, '_p1', '', '', '\"\"', 0, 0)",
                "query04": "CALL spProyectosDirecciones(4, '_p1', '_p2', '_p3', '\"\"', 0, 0)",
                "query05": "CALL spProyectosDirecciones(5,   '' , '', '', '_pkToDelete', 0, 0)",
                "query06": "CALL spProyectosDirecciones(6, '_p1', '_p2', '', '\"\"', 0, 0)",
            }, 
            # PROYECTOS REPORTE ATENCIÓN
            {
                "entidad": "proyectoreporteatencion",
                "query"  : [],
                "head": ["", 'PROYECTO','TITULO','LICITACION','FOLIO','FECHA_DESDE','FECHA_HASTA','CANTIDAD_LENTES',
                         'TOTAL_ATENCIONES','OC_MANDANTE','FECHA_VB','FA_NUMERO','FA_FECHA','FA_TOTAL','NC_NUMERO',
                         'NC_FECHA','NC_TOTAL','ND_NUMERO','ND_FECHA','ND_TOTAL','GUIA_NUMERO','GUIA_FECHA','OBSERVACIONES'],
                "params" : ["_p1", "_p2", '_p3', '_pkToDelete' ,'_id'],
                "def"    : ["", "", "", "\"\"", "0"],
                "query01": "CALL spProyectosReporteAtencion(1, '_p1', '_p2', '_p3', '\"\"', _id, 0)",
                "query03": "CALL spProyectosReporteAtencion(3, '_p1', '', '', '\"\"', 0, 0)",
                "query04": "CALL spProyectosReporteAtencion(4, '_p1', '_p2', '_p3', '\"\"', 0, 0)",
                "query05": "CALL spProyectosReporteAtencion(5,   '' , '', '', '_pkToDelete', 0, 0)",
                "query06": "CALL spProyectosReporteAtencion(6, '_p1', '_p2', '_p3', '', 0, 0)",
            }, 
            # PROYECTOS REPORTE FIRMAS
                {
                "entidad": "proyectoreportefirma",
                "query"  : [],
                "head": ["", 'PROYECTO','TITULO','LICITACION','FOLIO_REPORTE','FECHA_DESDE','FECHA_HASTA','OBSERVACIONES'],
                "params" : ["_p1", "_p2", '_p3', '_pkToDelete' ,'_id'],
                "def"    : ["", "", "", "\"\"", "0"],
                "query01": "CALL spProyectosReporteFirma(1, '_p1', '_p2', '_p3', '\"\"', _id, 0)",
                "query03": "CALL spProyectosReporteFirma(3, '_p1', '', '', '\"\"', 0, 0)",
                "query04": "CALL spProyectosReporteFirma(4, '_p1', '_p2', '_p3', '\"\"', 0, 0)",
                "query05": "CALL spProyectosReporteFirma(5,   '' , '', '', '_pkToDelete', 0, 0)",
                "query06": "CALL spProyectosReporteFirma(6, '_p1', '_p2', '', '', 0, 0)",
            }, 
            # OFTALMÓLOGOS
            {
                "entidad": "oftalmologos",
                "query"  : [],
                "head"   : ["", "ID", "RUT", "NOMBRE", "TELÉFONO", "CORREO", "VALOR CONSULTA"],
                "params" : ["_p1", "_p2", "_p3","_id"],
                "def"    : ["", "0", "", "0"],
                "query01": "CALL spOftalmologos(1, '_p1', 0, '_p3', _id, 0)",
                "query02": "CALL spOftalmologos(2,   '' , 0,'', 0, 0)",
                "query03": "CALL spOftalmologos(3, '_p1', 0, '', 0, 0)",
                "query04": "CALL spOftalmologos(4, '_p1', _p2, '', 0, 0)",
                "query05": "CALL spOftalmologos(5, '_p1', 0, '', 0, 0)",
            },


            # *********** S I S T E M A *********** 
            # USUARIOS
            {
                "entidad": "usuarios",
                "query": [],
                "head": ["","ID","NOMBRE", "TELEFONO", "CORREO","ESTADO", "CARGO ID", "CARGO"],
                "params": ["_p1", "_p2", "_p3","_id"],
                "def": ["", "0", "", "0"],
            "query01": "CALL spUsuarios(1, '_p1', _p2,'', _id, 0)",
            "query02": "CALL spUsuarios(2,   '' , 0,'', 0, 0)",
            "query03": "CALL spUsuarios(3, '_p1', 0, '', 0, 0)",
            "query04": "CALL spUsuarios(4, '_p1', _p2, \"_p3\", 0, 0)",
            "query05": "CALL spUsuarios(5, '_p1', 0, '', 0, 0)",
            "query06": "CALL spUsuarios(6, '_p1', 0, '_p3', 0,0)",
            "query07": "CALL spUsuarios(7, '_p1', 0, '', 0, 0)",
            "query08": "CALL spUsuarios(8,   '' , 0, '', _id, 0)",
            "query99": "CALL spUsuarios(99,  '' , 0, '', _id, 0)",
            },
            # CARGOS
            {
                "entidad": "cargos",
                "query"  : [],
                "head"   : ["","ID", "CARGO", "USUARIOS"],
                "params" : ["_p1", "_p2",'_id'],
                "def"    : ["", "0","0"],
                "query01": "CALL spCargos(1, '_p1', _p2,_id, 0)",
                "query02": "CALL spCargos(2,   '' ,   0, 0, 0)",
                "query03": "CALL spCargos(3, '_p1',   0, 0, 0)",
                "query04": "CALL spCargos(4, '_p1', _p2, 0, 0)",
                "query05": "CALL spCargos(5, '_p1',   0, 0, 0)",
            },
            # FUNCIONALIDADES
            {
                "entidad": "funcionalidades",
                "query"  : [],
                "head"   : ["","ID", "FUNCIONALIDAD"],
                "params" : ["_p1", "_p2",'_id'],
                "def"    : ["", "0","0"],
                "query01": "CALL spFuncionalidades(1, '_p1', _p2,_id, 0)",
                "query02": "CALL spFuncionalidades(2,   '' , 0, 0, 0)",
                "query03": "CALL spFuncionalidades(3, '_p1', 0, 0, 0)",
                "query04": "CALL spFuncionalidades(4, '_p1', _p2, 0, 0)",
                "query05": "CALL spFuncionalidades(5, '_p1', 0, 0, 0)",
            },
            # PERFILES
            {
                "entidad": "perfiles",
                "query"  : [],
                "head"   : ["", "CARGO_ID", "CARGO", "FUNCIONALIDAD_ID", "FUNCIONALIDAD","PERMISO"],
                "params" : ["_p1", "_p2", "_p3", '_pkToDelete', '_id'],
                "def"    : ["", "0", "0", "", "0"],
                "query01": "CALL spPerfiles(1,   '' , '_p2', '_p3', '\"\"', _id, 0)",
                "query03": "CALL spPerfiles(3, '_p1',    0 ,   0  , '\"\"', 0, 0)",
                "query04": "CALL spPerfiles(4, '_p1',   _p2,  _p3 , '\"\"', 0, 0)",
                "query05": "CALL spPerfiles(5,   '' ,    0 ,   0  , '_pkToDelete', 0, 0)",
            },
            # PERMISOS
            {
                "entidad": "permisos",
                "query"  : [],
                "head"   : ["", "USUARIO_ID", "USUARIO", "FUNCIONALIDAD_ID", "FUNCIONALIDAD", "PERMISO"],
                "params" : ["_p1", "_p2", "_p3", '_pkToDelete', '_id'],
                "def"    :["", "0", "0", "", "0"],
                "query01": "CALL spPermisos(1,   '' , '_p2', '_p3', '\"\"', _id, 0)",
                "query03": "CALL spPermisos(3, '_p1',    0 , 0, '\"\"', 0, 0)",
                "query04": "CALL spPermisos(4, '_p1',  _p2 , _p3, '\"\"', 0, 0)",
                "query05": "CALL spPermisos(5,   '' ,    0 , 0, '_pkToDelete', 0, 0)",
                "query06": "CALL spPermisos(6,   '' ,  _p2 , 0, '\"\"', 0, 0)",
            },
            # OT PERMISOS
            {
                "entidad": "otpermisos",
                "query"  : [],
                "head"   : ["", "USUARIO_ID", "USUARIO", "AREA_ID", "AREA", "PERMISO"],
                "params" : ["_p1", "_p2", "_p3", '_pkToDelete', '_id'],
                "def"    :["", "0", "0", "", "0"],
                "query01": "CALL spOTPermisos(1, '', '_p2', '_p3', '\"\"', _id, 0)",
                "query03": "CALL spOTPermisos(3, '_p1', 0, 0, '\"\"', 0, 0)",
                "query04": "CALL spOTPermisos(4, '_p1', _p2, _p3, '\"\"', 0, 0)",
                # "query05": "CALL spOTPermisos(5, '_p1', 0, '', 0, 0)",
            },
            # OT FUNCIONALIDADES
            {
                "entidad": "otfuncionalidades",
                "query"  : [],
                "head"   : ["","ID", "FUNCIONALIDAD OT"],
                "params" : ["_p1", "_p2",'_id'],
                "def"    : ["", "0","0"],
                "query02": "CALL spOTFuncionalidades(2, '', 0, 0, 0)",
            },

            # EMPRESAS
            {
            "entidad": "empresas",
            "query": [],
            "head": ["", "ID", "RUT", "NOMBRE", "RAZON SOCIAL", "GIRO", "DIRECCION", "TELEFONO", 
                     "CORREO", "SITIO WEB"],
                "params": ["_p1", "_p2", "_p3","_id"],
                "def": ["", "0", "", "0"],
                "query01": "CALL spEmpresas(1, '_p1', 0, '_p3', _id, 0)",
                "query02": "CALL spEmpresas(2, '', 0,'', 0, 0)",
                "query03": "CALL spEmpresas(3, '_p1', 0, '', 0, 0)",
                "query04": "CALL spEmpresas(4, '_p1', _p2, '', 0, 0)",
                "query05": "CALL spEmpresas(5, '_p1', 0, '', 0, 0)",
            },
            # TIPOS
            {
                "entidad": "tipos",
                "query": [],
                "params": ["_p1", "_id"],
                "def": ["", "0"],
            "query02": "CALL spTipos(1,'_p1', '0', '', 0)",
            },
            
            # KARDEXMOTIVOS
            {
                "entidad": "kardexmotivos",
                "query": [],
                "params": ["_p1"],
                "def": ["0"],
            "query01": "CALL spKardexMotivos(1)", #Motivos de Entrada Bodega
            "query02": "CALL spKardexMotivos(2)", #Motivos de Salida Bodega
            },
            # COMUNAS
            {
                "entidad": "comunas",
                "query"  : [],
                "params" : ["_p1"],
                "def"    : ["0"],
                "query02": "CALL spRegProCom(1, _p1)",
            },
            # PROVINCIAS
            {
                "entidad": "provincias",
                "query"  : [],
                "params" : ["_p1"],
                "def"    : ["0"],
                "query02": "CALL spRegProCom(2, _p1)",
            },
            # REGIONES
            {
                "entidad": "regiones",
                "query"  : [],
                "params" : ["_p1"],
                "def"    : ["0"],
                "query02": "CALL spRegProCom(3, _p1)",
            },
            # PARAMETROS
            {
                "entidad": "parametros",
                "query": [],
                "head": [''],
                "params": ["_p1", '_id'],
                "def": ["", "0"],
                "query01": "CALL spParametros(1, '_p1', _id, 0)",
                "query02": "CALL spParametros(2, '_p1',   0, 0)",
            },

        ]