pref = ""
table_query = [
    # *********** O T *********** 
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
        "query03": "CALL spClientes(3, \"_p1\", '', 0, '\"\"', 0, 0)",
        "query04": "CALL spClientes(4, \"_p1\", _p2, 0, '\"\"', 0, 0)",
        "query05": "CALL spClientes(5, '', '', 0, '_pkToDelete', 0, 0)",
    },
    # ESTABLECIMIENTOS
    {
        "entidad": "establecimientos",
        "query"  : [],
        "head"   : ["", "ID", "NOMBRE", "MANDANTE", "MANDANTE_ID", "REGION_ID", "REGION", "PROVINCIA_ID", "PROVINCIA", "COMUNA_ID", "COMUNA"],
        "params" : ["_p1", "_p2", "_id"],
        "def"    : ["", "0", "0"],
        "query01": "CALL spEstablecimientos(1, '_p1', _p2, _id, 0)",
        "query02": "CALL spEstablecimientos(2, '_p1 ', 0, 0, 0)",
        "query03": "CALL spEstablecimientos(3, \"_p1\", 0, 0, 0)",
        "query04": "CALL spEstablecimientos(4, \"_p1\", _p2, 0, 0)",
        "query05": "CALL spEstablecimientos(5, '_p1', 0, 0, 0)",
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
        "query02": "CALL spPuntosVenta(2, '', 0, 0, 0)",
        "query03": "CALL spPuntosVenta(3, \"_p1\", 0, 0, 0)",
        "query04": "CALL spPuntosVenta(4, \"_p1\", _p2, 0, 0)",
        "query05": "CALL spPuntosVenta(5, '_p1', 0, 0, 0)",
    },
    
    # *********** B O D E G A *********** 
    # ARMAZONES
    {
        "entidad": "armazones",
        "query": [],
        "head": ["", 'CODIGO', 'ARMAZON_TIPO_ID', 'ARMAZON_TIPO', 'MARCA_ID', 'MARCA', 'MODELO', 'COLOR', 
                 'ARMAZON_MATERIAL_ID', 'ARMAZON_MATERIAL', 'ARO', 'PUENTE', 'DIAGONAL', 'BRAZO', 'ARMAZON_USO_ID',
                 'ARMAZON_USO', 'STOCK_MINIMO'],
        "params": ["_p1", "_p2", "_p3", "_id"],
        "def": ["", "", "0", "0"],
        "query01": "CALL spArmazones(1, '_p1', '_p2', _p3, _id, 0)",
        "query02": "CALL spArmazones(2, '', '', 0, 0, 0)",
        "query03": "CALL spArmazones(3, \"_p1\", '', 0, 0, 0)",
        "query04": "CALL spArmazones(4, \"_p1\", '', _p3, 0, 0)",
        "query05": "CALL spArmazones(5, '_p1', '', 0, 0, 0)",
    },
    # CRISTALES
    {
        "entidad": "cristales",
        "query"  : [],
        "head"   : ["", 'CODIGO', 'MARCA_ID', 'MARCA', 'PROVEEDOR_ID', 'PROVEEDOR', 'DISENO_ID', 'DISENO',
                    'INDICE_ID', 'INDICE', 'MATERIAL_ID', 'MATERIAL', 'COLOR_ID', 'COLOR',
                    'TRATAMIENTO_ID', 'TRATAMIENTO', 'DIAMETRO', 'ESFERICO', 'CILINDRICO', 'STOCK_MINIMO'],
        "params" : ["_p1", "_p2", "_pMarca","_pProveedor","_pDiseno", "_pIndice","_pMaterial", 
                    "_pColor", "_pTratamiento","_pDiametro", "_pEsferico","_pCilindrico", "_id"],
        "def"    : ["0", "", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        "query01": "CALL spCristales(1, '_p1'  , '' , _pMarca, _pProveedor, _pDiseno, _pIndice, _pMaterial, _pColor, _pTratamiento, _pDiametro, _pEsferico, _pCilindrico, _id, 0);",
        "query02": "CALL spCristales(2, ''     , '' , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);", #SELECT codigo, codigo FROM C...
        "query03": "CALL spCristales(3, \"_p1\", '' , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
        "query04": "CALL spCristales(4, \"_p1\", _p2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
        "query05": "CALL spCristales(5, '_p1'  , 0  , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
    },
    # CRISTALES KARDEX
    {
        "entidad": "cristaleskardex",
        "query"  : [],
        "head"   : ["", 'FECHA', 'CRISTAL', 'DESCRIPCION', 'ALMACEN_ID', 'ALMACEN', 'ES', 'MOTIVO_ID', 'MOTIVO', 
                    'ENTRADAS', 'SALIDAS', 'VALOR_NETO', 'PROVEEDOR_ID', 'PROVEEDOR', 'FACTURA',
                    'OT', 'ALMACEN_RELACIONADO_ID', 'ALMACEN_RELACIONADO', 'OBSERVACIONES'],
        "params" : ["_p1", "_p2", "_p3", "_pkToDelete", "_pAlmacen", "_pMarca","_pProveedor","_pDiseno", 
                    "_pIndice","_pMaterial", "_pColor", "_pTratamiento","_pDiametro", "_pEsferico","_pCilindrico", "_id"],
        "def"    : ["0", "0", "", "", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        "query01": "CALL spCristalesKardex(1, '_p1'  , '' , ''     , '\"\"', _pAlmacen, _pMarca, _pProveedor, _pDiseno, _pIndice, _pMaterial, _pColor, _pTratamiento, _pDiametro, _pEsferico, _pCilindrico, _id, 0);",
        "query03": "CALL spCristalesKardex(3, \"_p1\", '' , ''     , '\"\"', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
        "query04": "CALL spCristalesKardex(4, \"_p1\", '_p2', '_p3', '\"\"', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
        "query05": "CALL spCristalesKardex(5, ''  , '' , '' ,   '_pkToDelete', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);",
    },
    # ACCESORIOS
    {
        "entidad": "accesorios",
        "query": [],
        "head": ["", "CODIGO", "DESCRIPCION", "PROVEEDOR_ID", "PROVEEDOR", "PRECIO_NETO", "STOCK_MINIMO"],
        "params": ["_p1", "_p2", "_p3", "_id"],
        "def": ["", "", "0", "0"],
        "query01": "CALL spAccesorios(1, '_p1', '_p2', _p3, _id, 0)",
        "query02": "CALL spAccesorios(2, '', '', 0, 0, 0)",
        "query03": "CALL spAccesorios(3, \"_p1\", '', 0, 0, 0)",
        "query04": "CALL spAccesorios(4, \"_p1\", _p2, 0, 0, 0)",
        "query05": "CALL spAccesorios(5, '_p1', '', 0, 0, 0)",
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
        "query03": "CALL spProveedores(3, \"_p1\", 0, '', 0, 0)",
        "query04": "CALL spProveedores(4, \"_p1\", _p2, '', 0, 0)",
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
        "query03": "CALL spAlmacenes(3, \"_p1\", 0, 0, 0)",
        "query04": "CALL spAlmacenes(4,\"_p1\", _p2, 0, 0)",
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
        "query03": "CALL spMarcas(3, \"_p1\", 0, 0, 0)",
        "query04": "CALL spMarcas(4,\"_p1\", _p2, 0, 0)",
        "query05": "CALL spMarcas(5, '_p1', 0, 0, 0)",
    },

    # *********** P R O Y E C T O S *********** 
    # OFTALMÓLOGOS
    {
        "entidad": "oftalmologos",
        "query"  : [],
        "head"   : ["", "ID", "RUT", "NOMBRE", "TELEFONO", "CORREO", "VALOR_CONSULTA"],
        "params" : ["_p1", "_p2", "_p3","_id"],
        "def"    : ["", "0", "", "0"],
        "query01": "CALL spOftalmologos(1, '_p1', 0, '_p3', _id, 0)",
        "query02": "CALL spOftalmologos(2, '', 0,'', 0, 0)",
        "query03": "CALL spOftalmologos(3, \"_p1\", 0, '', 0, 0)",
        "query04": "CALL spOftalmologos(4, \"_p1\", _p2, '', 0, 0)",
        "query05": "CALL spOftalmologos(5, '_p1', 0, '', 0, 0)",
    },
    # MANDANTES
    {
        "entidad": "mandantes",
        "query"  : [],
        "head"   : ["", "CODIGO", "RUT", "NOMBRE", "REGION_ID", "REGION", "PROVINCIA_ID", "PROVINCIA", "COMUNA_ID", "COMUNA"],
        "params" : ["_p1", "_p2", '_pkToDelete', "_id"],
        "def"    : ["", "", "", "0"],
        "query01": "CALL spMandantes(1, '_p1', '_p2', '\"\"', _id, 0)",
        "query02": "CALL spMandantes(2, '', '', '\"\"', 0, 0)",
        "query03": "CALL spMandantes(3, \"_p1\", '', '\"\"', 0, 0)",
        "query04": "CALL spMandantes(4, \"_p1\", \"_p2\", '\"\"', 0, 0)",
        "query05": "CALL spMandantes(5, '', '', '_pkToDelete', 0, 0)",
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
       "query02": "CALL spUsuarios(2, '', 0,'', 0, 0)",
       "query03": "CALL spUsuarios(3, \"_p1\", 0, '', 0, 0)",
       "query04": "CALL spUsuarios(4,\"_p1\", _p2, \"_p3\", 0, 0)",
       "query05": "CALL spUsuarios(5, '_p1', 0, '', 0, 0)",
       "query06": "CALL spUsuarios(6, '_p1', 0, '_p3', 0,0)",
       "query07": "CALL spUsuarios(7, '_p1', 0, '', 0, 0)",
       "query08": "CALL spUsuarios(7, '', 0, '', _id, 0)"
    },
    # CARGOS
    {
        "entidad": "cargos",
        "query"  : [],
        "head"   : ["","ID", "CARGO"],
        "params" : ["_p1", "_p2",'_id'],
        "def"    : ["", "0","0"],
        "query01": "CALL spCargos(1, '_p1', _p2,_id, 0)",
        "query02": "CALL spCargos(2, '', 0, 0, 0)",
        "query03": "CALL spCargos(3, \"_p1\", 0, 0, 0)",
        "query04": "CALL spCargos(4,\"_p1\", _p2, 0, 0)",
        "query05": "CALL spCargos(5, '_p1', 0, 0, 0)",
    },
    # FUNCIONALIDADES
    {
        "entidad": "funcionalidades",
        "query"  : [],
        "head"   : ["","ID", "FUNCIONALIDAD"],
        "params" : ["_p1", "_p2",'_id'],
        "def"    : ["", "0","0"],
        "query01": "CALL spFuncionalidades(1, '_p1', _p2,_id, 0)",
        "query02": "CALL spFuncionalidades(2, '', 0, 0, 0)",
        "query03": "CALL spFuncionalidades(3, \"_p1\", 0, 0, 0)",
        "query04": "CALL spFuncionalidades(4,\"_p1\", _p2, 0, 0)",
        "query05": "CALL spFuncionalidades(5, '_p1', 0, 0, 0)",
    },
    # PERFILES
    {
        "entidad": "perfiles",
        "query"  : [],
        "head"   : ["", "CARGO_ID", "CARGO", "FUNCIONALIDAD_ID", "FUNCIONALIDAD","PERMISO"],
        "params" : ["_p1", "_p2", "_p3", '_pkToDelete', '_id'],
        "def"    : ["", "0", "0", "", "0"],
        "query01": "CALL spPerfiles(1, '', '_p2', '_p3', '\"\"', _id, 0)",
        "query03": "CALL spPerfiles(3, '_p1', 0, 0, '\"\"', 0, 0)",
        "query04": "CALL spPerfiles(4, '_p1', _p2, _p3, '\"\"', 0, 0)",
        "query05": "CALL spPerfiles(5, '', 0, 0, '_pkToDelete', 0, 0)",
    },
    # PERMISOS
    {
        "entidad": "permisos",
        "query"  : [],
        "head"   : ["", "USUARIO_ID", "USUARIO", "FUNCIONALIDAD_ID", "FUNCIONALIDAD", "PERMISO"],
        "params" : ["_p1", "_p2", "_p3", '_pkToDelete', '_id'],
        "def"    :["", "0", "0", "", "0"],
        "query01": "CALL spPermisos(1, '', '_p2', '_p3', '\"\"', _id, 0)",
        "query03": "CALL spPermisos(3, '_p1', 0, 0, '\"\"', 0, 0)",
        "query04": "CALL spPermisos(4, '_p1', _p2, _p3, '\"\"', 0, 0)",
        "query05": "CALL spPermisos(5, '', 0, 0, '_pkToDelete', 0, 0)",
        "query06": "CALL spPermisos(6, '', _p2, 0, '\"\"', 0, 0)",
    },
    # EMRPESAS
    {
       "entidad": "empresas",
       "query": [],
       "head": ["", "ID", "RUT", "NOMBRE", "RAZON SOCIAL", "GIRO", "DIRECCION", "TELEFONO", "CORREO", "SITIO WEB", "NOMBRE LOGO"],
        "params": ["_p1", "_p2", "_p3","_id"],
        "def": ["", "0", "", "0"],
        "query01": "CALL spEmpresas(1, '_p1', 0, '_p3', _id, 0)",
        "query02": "CALL spEmpresas(2, '', 0,'', 0, 0)",
        "query03": "CALL spEmpresas(3, \"_p1\", 0, '', 0, 0)",
        "query04": "CALL spEmpresas(4, \"_p1\", _p2, '', 0, 0)",
        "query05": "CALL spEmpresas(5, '_p1', 0, '', 0, 0)",
    },
    # TIPOS
    {
        "entidad": "tipos",
        "query": [],
        "params": ["_p1"],
        "def": [""],
       "query02": "CALL spTipos('_p1')",
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

]