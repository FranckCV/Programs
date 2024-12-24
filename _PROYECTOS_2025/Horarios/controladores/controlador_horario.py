from controladores.bd import obtener_conexion

def obtener_horarios():
    conexion = obtener_conexion()
    # try:
    with conexion.cursor() as cursor:
        sql = '''
            select 
                hor.id, 
                hor.dia, 
                hor.h_inicio, 
                hor.h_final, 
                gr.denominacion, 
                gr.semestrecodigo, 
                cur.nombre, 
                cur.abreviacion, 
                cur.color, 
                cur.ciclo, 
                doc.nombres, 
                doc.apellidos 
            from grupo gr 
            inner join docente doc on doc.id = gr.docenteid 
            inner join curso cur on cur.id = gr.cursoid 
            inner join horario hor on hor.grupoid = gr.id
        '''
        cursor.execute(sql)
        elementos = cursor.fetchall() 
    conexion.close()
    return elementos
    # except Exception as e:
    #     return e

# def obtener_cantidad_grupo():
#     conexion = obtener_conexion()
#     try:
#         with conexion.cursor() as cursor:
#             sql= "select id, nomgrupo from grupo"
#             cursor.execute(sql)
#             grupos = cursor.fetchall()
#         conexion.close()
#         return grupos
#     except Exception as e:
#         return e



# def funcion_prueba_jpd():
#     conexion = obtener_conexion()
#     try:
#         with conexion.cursor() as cursor:
#             sql = """
#                 SELECT e.id AS ElementoID, e.nomElemento AS Elemento, COUNT(c.id) AS CantidadCualidades
#                 FROM elemento e
#                 LEFT JOIN cualidad c ON e.id = c.ELEMENTOid
#                 GROUP BY e.id, e.nomElemento;
#             """
#             cursor.execute(sql)
#             pruebita = cursor.fetchall() 
#         conexion.close()
#         return pruebita
#     except Exception as e:
#         return e


# def obtener_grupo_incompleto(participante_id):
#     conexion = obtener_conexion()
#     try:
#         with conexion.cursor() as cursor:
#             sql = """
#                 SELECT g.id
#                 FROM grupo g
#                 LEFT JOIN (
#                     SELECT s.AGRUPACIONGRUPOid, COUNT(*) AS seleccionadas
#                     FROM seleccion s
#                     WHERE s.PARTICIPANTEid = %s
#                     GROUP BY s.AGRUPACIONGRUPOid
#                 ) AS conteo
#                 ON g.id = conteo.AGRUPACIONGRUPOid
#                 WHERE IFNULL(conteo.seleccionadas, 0) < (SELECT COUNT(*) FROM agrupacion WHERE GRUPOid = g.id)
#                 LIMIT 1;
#             """
#             cursor.execute(sql, (participante_id,))
#             resultado = cursor.fetchone()
#             return resultado[0] if resultado else None
#     except Exception as e:
#         print(f"Error al obtener el grupo incompleto: {str(e)}")
#         return None
#     finally:
#         conexion.close()


# def obtener_cantidad_maxima_progreso():
#     conexion = obtener_conexion()
#     # try:
#     with conexion.cursor() as cursor:
#         sql= "select count(*) from grupo"
#         cursor.execute(sql)
#         grupos = cursor.fetchone()
#         numero = grupos[0] * 2
#     conexion.close()
#     return numero
#     # except Exception as e:
#     #     return e
    


