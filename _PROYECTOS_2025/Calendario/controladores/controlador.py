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
                act.prioridad ,
                act.color ,

                act.h_fin * 60 + act.min_fin - (act.h_ini + 1) * 60 + 60 - act.min_ini ,

                act.id 
            from actividad act 
        '''
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos


def obtener_total_minutos_acts():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = '''
            select SUM(act.h_fin * 60 + act.min_fin - (act.h_ini + 1) * 60 + 60 - act.min_ini) from actividad act;
        '''
        cursor.execute(sql)
        elementos = cursor.fetchone() 
    conexion.close()
    return elementos[0]


def obtener_max_minuto_acts():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = '''
            SELECT MAX(act.`min_ini`) , MAX(act.`min_fin`) FROM `actividad` act;
        '''
        cursor.execute(sql)
        elementos = cursor.fetchone() 
    conexion.close()
    return elementos[0]



