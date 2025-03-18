from flask import Flask, render_template, request, redirect, flash, jsonify, session, make_response,  redirect, url_for
from datetime import datetime, date , timedelta
import hashlib
import base64
import controladores.controlador as controlador

app = Flask(__name__, template_folder='templates')

##########_ CONSTANTES _##########

BASE_NOMBRE_DIAS = ('DOMINGO','LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO')
TOTAL_DAYS = 7
DIF_DAYS = 1
DIF_HOURS = 1
TIME_MIN = 15
CANTCOLSAD = 3
CANTROWSAD = 2

sizeCOL   = '150px'
sizeCOLad = '30px'
sizeROW   = '17px'
sizeROWad = '17px'
sizeGAP   = '3px'


now = datetime.now()
date_day = now.weekday()
current_day = ( date_day + 1 ) % 7
# current_hour = 13 
current_hour = now.hour   
current_minute = now.minute



##########_ FUNCIONES _##########

def listarDias():
    lista = []
    for day in range(TOTAL_DAYS) :
        ddd = (day + current_day - DIF_DAYS) % 7
        lista.append(ddd)
    return lista


def listarHoras():
    lista = []
    for hour in range(24) :
        hhh = (hour + current_hour - DIF_HOURS) % 24
        lista.append(hhh)
    return lista


def listarMinutos():
    lista = []
    for min in range(60) :
        if min % TIME_MIN == 0:
            lista.append(min)
    return lista

def listarFechas():
    lista = []
    for number in range(TOTAL_DAYS) :
        date = now + timedelta(days = number - DIF_DAYS)
        lista.append(date.strftime("%d/%m/%Y"))
    return lista


BASE_dias = listarDias()
BASE_horas = listarHoras()
BASE_minutos = listarMinutos()
BASE_fechas = listarFechas()





def actualizar_tiempo():
    global now, current_day, current_hour, current_minute, BASE_dias, BASE_horas, BASE_minutos , BASE_fechas
    
    now = datetime.now()
    date_day = now.weekday()
    current_day = (date_day + 1) % 7 
    # current_hour = 13
    current_hour = now.hour
    current_minute = now.minute

    BASE_dias = listarDias()
    BASE_horas = listarHoras()
    BASE_minutos = listarMinutos()
    BASE_fechas = listarFechas()



##########_ RUTAS _##########

@app.route("/")
def index():
    actualizar_tiempo()

    actividades = controlador.obtener_acts()
    cantCol = len(BASE_dias)
    cantRow = ( len(BASE_horas) * len(BASE_minutos) )
    cantHor = len(BASE_horas)
    cantMin = len(BASE_minutos)
    spaces = cantCol * cantRow
    # print(spaces)
    return render_template(
        "horario.html" , 
        spaces = spaces , 
        actividades = actividades ,
        cantCol = cantCol ,
        cantRow = cantRow ,
        CANTCOLSAD = CANTCOLSAD ,
        CANTROWSAD = CANTROWSAD ,
        BASE_NOMBRE_DIAS = BASE_NOMBRE_DIAS ,
        BASE_dias = BASE_dias, 
        BASE_horas = BASE_horas,
        BASE_minutos = BASE_minutos ,
        BASE_fechas = BASE_fechas ,
        cantHor = cantHor ,
        cantMin = cantMin ,
        sizeCOL = sizeCOL ,
        sizeCOLad = sizeCOLad ,
        sizeROW = sizeROW ,
        sizeROWad = sizeROWad ,
        DIF_DAYS = DIF_DAYS ,
        sizeGAP = sizeGAP , 

        )







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)






# @app.context_processor
# def inject_globals():
#     return dict(
        
#     )
