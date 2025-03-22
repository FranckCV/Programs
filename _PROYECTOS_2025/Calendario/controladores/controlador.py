from controladores.bd import obtener_conexion
from datetime import datetime, date , timedelta 

def formato_fecha_bd(date):
    return date.strftime("%Y-%m-%d")


def obtener_max_minuto_acts():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = '''
            SELECT MAX(hor.`min_ini`) , MAX(hor.`min_fin`) FROM `horario` hor;
        '''
        cursor.execute(sql)
        elementos = cursor.fetchone() 
    conexion.close()

    if elementos[0] < elementos[1]:
        return elementos[1]
    else:
        return elementos[0]


def obtener_acts():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        sql = '''
            select 
                ctx.id ,

                ctx.nombre ,
                ctx.descripcion ,
                hor.dia ,
                
                hor.h_ini ,
                hor.min_ini ,
                hor.h_fin ,
                hor.min_fin ,

                hor.fecha_ini ,
                hor.fecha_fin ,
                ctx.id ,
                ctx.color ,

                hor.h_fin * 60 + hor.min_fin - (hor.h_ini + 1) * 60 + 60 - hor.min_ini ,

                ctx.id 
            from horario hor 
            inner join contexto ctx on ctx.id = hor.contextoid
        '''
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos


def obtener_horarios_fecha():
    conexion = obtener_conexion()

    # fechamod = fecha
    # print(fechamod)

    with conexion.cursor() as cursor:
        sql = f'''
            select 
                ctx.id ,

                ctx.nombre ,
                ctx.color ,
                hor.dia ,
                
                hor.h_ini ,
                hor.min_ini ,
                hor.h_fin ,
                hor.min_fin ,

                hor.fecha_ini ,
                hor.fecha_fin ,
                ctx.id ,
                ctx.descripcion ,

                hor.h_fin * 60 + hor.min_fin - (hor.h_ini + 1) * 60 + 60 - hor.min_ini ,

                ctx.id 
            from horario hor 
            inner join contexto ctx on ctx.id = hor.contextoid
            where hor.fecha_ini <= CURRENT_DATE and CURRENT_DATE <= hor.fecha_fin
        '''
        # print(sql)
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos


def obtener_tareas_fecha():
    conexion = obtener_conexion()

    with conexion.cursor() as cursor:
        sql = f'''
            select 
                ctx.id ,

                ctx.nombre ,
                ctx.color ,
                ctx.descripcion ,

                hor.dia ,
                
                hor.h_ini ,
                hor.min_ini ,
                hor.h_fin ,
                hor.min_fin ,

                hor.fecha_ini ,
                hor.fecha_fin ,

                hor.titulo ,
                hor.descripcion ,

                ctx.letras ,
                ctx.icono ,
                ctx.img ,

                hor.id 
            from contexto ctx 
            left join horario hor on ctx.id = hor.contextoid
            where hor.fecha_ini <= CURRENT_DATE and CURRENT_DATE <= hor.fecha_fin 
            order by
                CASE 
                    WHEN hor.dia >= (DAYOFWEEK(CURRENT_DATE) + 1) THEN 0 
                    ELSE 1  
                END,
                hor.dia, 
                hor.h_ini, 
                hor.min_ini, 
                hor.h_fin;

        '''
        # print(sql)
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos


def obtener_tareas_hoy():
    conexion = obtener_conexion()

    # fechamod = fecha.strftime("%Y-%m-%d")
    # dia = fecha.weekday() + 1
    # hora = fecha.hour  

    with conexion.cursor() as cursor:
        sql = f'''
            select 
                ctx.id ,

                ctx.nombre ,
                ctx.color ,
                ctx.descripcion ,

                hor.dia ,
                
                hor.h_ini ,
                hor.min_ini ,
                hor.h_fin ,
                hor.min_fin ,

                hor.fecha_ini ,
                hor.fecha_fin ,

                hor.titulo ,
                hor.descripcion ,

                ctx.letras ,
                ctx.icono ,
                ctx.img ,

                hor.id 
            from contexto ctx 
            left join horario hor on ctx.id = hor.contextoid
            where hor.fecha_ini <= CURRENT_DATE
            and CURRENT_DATE <= hor.fecha_fin 
            and  hor.dia = (DAYOFWEEK(CURRENT_DATE) - 1 ) % 7
            and (HOUR(CURRENT_TIME)) < hor.h_fin 

            order by hor.h_ini , hor.min_ini , hor.h_fin
        '''
        # or ( hor.dia = (DAYOFWEEK(CURRENT_DATE) )
        # print(sql)
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos


def obtener_tareas_sinfecha():
    conexion = obtener_conexion()

    with conexion.cursor() as cursor:
        sql = f'''
            select 
                ctx.id ,

                ctx.nombre ,
                ctx.color ,
                ctx.descripcion ,

                hor.dia ,
                
                hor.h_ini ,
                hor.min_ini ,
                hor.h_fin ,
                hor.min_fin ,

                hor.fecha_ini ,
                hor.fecha_fin ,

                hor.titulo ,
                hor.descripcion ,

                ctx.letras ,
                ctx.icono ,
                ctx.img ,

                hor.id 
            from horario hor 
            left join contexto ctx on ctx.id = hor.contextoid
            where hor.fecha_ini is NULL 
            and hor.fecha_fin is NULL
            and hor.dia is NULL

        '''
        # print(sql)
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos


def obtener_tareas_hoy_test(fecha):
    conexion = obtener_conexion()

    fechamod = fecha.strftime("%Y-%m-%d")
    dia = fecha.weekday() + 1
    hora = fecha.hour  

    with conexion.cursor() as cursor:
        sql = f'''
            select 
                ctx.id ,

                ctx.nombre ,
                ctx.color ,
                ctx.descripcion ,

                hor.dia ,
                
                hor.h_ini ,
                hor.min_ini ,
                hor.h_fin ,
                hor.min_fin ,

                hor.fecha_ini ,
                hor.fecha_fin ,

                hor.titulo ,
                hor.descripcion ,

                ctx.letras ,
                ctx.icono ,
                ctx.img ,

                hor.id 
            from contexto ctx 
            left join horario hor on ctx.id = hor.contextoid
            where hor.fecha_ini <= '{fechamod}' and '{fechamod}' <= hor.fecha_fin 
            and hor.dia = {dia} and {hora} <= hor.h_ini 
            order by hor.fecha_ini desc , hor.dia , hor.h_ini , hor.min_ini , hor.h_fin
        '''
        # print(sql)
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos




