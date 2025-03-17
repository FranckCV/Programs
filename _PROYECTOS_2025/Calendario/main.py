from flask import Flask, render_template, request, redirect, flash, jsonify, session, make_response,  redirect, url_for
from datetime import datetime, date , timedelta
# from flask_jwt import JWT, jwt_required, current_identity
# import uuid
# from functools import wraps
import hashlib
import base64
import controladores.controlador as controlador

# import controladores.controlador_horario as controlador_horario
# import controladores.controlador_curso as controlador_curso
# import controladores.controlador_color as controlador_color
# import controladores.controlador_matricula as controlador_matricula
# import controladores.controlador_alumno as controlador_alumno

app = Flask(__name__, template_folder='templates')


def listarHoras():
    lista = []
    for hour in range(24) :
        hhh = (hour + current_hour) % 24
        # date = now + timedelta(days = number)
        lista.append(hhh)
    return lista


def listarFechas():
    lista = []
    for number in BASE_DIAS :
        date = now + timedelta(days = number)
        lista.append(date.strftime("%d/%m/%Y"))
    return lista


now = datetime.now()
date_day = now.weekday()
current_day = date_day + 1 if date_day > 7 else ( date_day + 1 ) % 7
current_hour = now.hour   
current_minute = now.minute

BASE_NOMBRE_DIAS = ('DOMINGO','LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO')
BASE_DIAS = range(7)
# BASE_horas = (13,14,15,16,17,18,19,20,21,22,23,0,1,2,3,4,5,6,7,8,9,10,11,12)
BASE_horas = listarHoras()
BASE_MINUTOS = (0,15,30,45)

CANTCOLSAD = 2
CANTROWSAD = 1
sizeCOL = '155px'
sizeCOLad = '30px'
sizeROW = '20px'
sizeROWad = '1fr'


@app.route("/")
def index():
    actividades = controlador.obtener_acts()
    cantCol = len(BASE_DIAS)
    cantRow = ( len(BASE_horas) * len(BASE_MINUTOS) )- 1
    cantMin = len(BASE_MINUTOS)
    spaces = cantCol * cantRow
    return render_template(
        "horario.html" , 
        spaces = spaces , 
        actividades = actividades ,
        cantCol = cantCol ,
        cantRow = cantRow ,
        CANTCOLSAD = CANTCOLSAD ,
        CANTROWSAD = CANTROWSAD ,
        BASE_NOMBRE_DIAS = BASE_NOMBRE_DIAS ,
        BASE_DIAS = BASE_DIAS, 
        BASE_horas = BASE_horas,
        BASE_MINUTOS = BASE_MINUTOS ,
        cantMin = cantMin ,
        sizeCOL = sizeCOL ,
        sizeCOLad = sizeCOLad ,
        sizeROW = sizeROW ,
        sizeROWad = sizeROWad ,
        )




# print(current_day,current_hour,current_minute)


# # USUARIO_ID = 1
# # BASE_DIAS = (5,6,0,1,2,3,4,5,6,0)
# # HORAS_BASE = range(24)
# # BASE_MINUTOS = range(60)
# # BASE_MINUTOS = (0,5,10,15,20,25,30,35,40,45,50,55)

# @app.context_processor
# def inject_globals():
#     return dict(
        
#     )






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
