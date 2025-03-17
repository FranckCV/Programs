from controladores.bd import obtener_conexion

def obtener_acts():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = '''
            select 
                act.id ,

                act.nombre ,
                act.descripcion ,

                act.dia ,
                
                act.h_ini ,
                act.min_ini ,

                act.h_fin ,
                act.min_fin ,

                act.fecha_ini ,
                act.fecha_fin ,
                act.prioridad 
            from actividad act 
        '''
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos
