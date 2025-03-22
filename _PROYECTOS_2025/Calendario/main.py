from flask import Flask, render_template, request, redirect, flash, jsonify, session, make_response,  redirect, url_for
from datetime import datetime, date , timedelta 
import hashlib
import base64
import controladores.controlador as controlador
import pytz


def local_hour():
    return datetime.now(pytz.utc).astimezone(pytz.timezone('America/Lima'))


app = Flask(__name__, template_folder='templates')

##########_ CONSTANTES _##########

BASE_NOMBRE_DIAS = ('DOMINGO','LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO')
TOTAL_DAYS = 7
DIF_DAYS = 0
DIF_HOURS = 0
CANTCOLSAD = 3
CANTROWSAD = 2

HOUR_INI = 5
MIN_INI = 5

sizeCOL   = '150px'
sizeCOLad = '20px'
sizeROW   = '30px'
sizeROWad = '20px'
sizeGAP   = '1px'

now = local_hour()
date_day = now.weekday() + 1
current_day = ( date_day ) % 7
current_hour = now.hour   
current_minute = now.minute

time_min = 60 - controlador.obtener_max_minuto_acts()



##########_ FUNCIONES _##########

def formato_fecha_bd(date):
    return date.strftime("%Y-%m-%d")


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
        if min % time_min == 0:
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
    global now, current_day, current_hour, current_minute, BASE_dias, BASE_horas, BASE_minutos , BASE_fechas , time_min
    
    now = local_hour()
    date_day = now.weekday() + 1
    current_day = (date_day) % 7 
    current_hour = now.hour
    current_minute = now.minute

    time_min = 60 - controlador.obtener_max_minuto_acts()
    # time_min = 30

    BASE_dias = listarDias()
    BASE_horas = listarHoras()
    BASE_minutos = listarMinutos()
    BASE_fechas = listarFechas()



##########_ RUTAS _##########

ENLACES_MENU= [
    'index' ,
    'horario' ,
    'tareas' ,
    'sinfecha' ,
    # 'lista' ,
]


@app.context_processor
def inject_globals():
    actualizar_tiempo()
    
    horarios = controlador.obtener_horarios_fecha()
    tareas   = controlador.obtener_tareas_fecha()
    sinfecha = controlador.obtener_tareas_sinfecha()
    tareashoy = controlador.obtener_tareas_hoy()

    cantCol = len(BASE_dias)
    cantRow = ( len(BASE_horas) * len(BASE_minutos) )
    cantDay = len(BASE_dias)
    cantHor = len(BASE_horas)
    cantMin = len(BASE_minutos)
    spaces = cantCol * cantRow 

    return dict(
        horarios = horarios ,
        tareas = tareas,
        sinfecha = sinfecha,
        tareashoy = tareashoy ,

        spaces = spaces , 
        cantCol = cantCol ,
        cantRow = cantRow ,
        ENLACES_MENU = ENLACES_MENU,
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
        DIF_HOURS = DIF_HOURS ,
        sizeGAP = sizeGAP , 
        current_day = current_day ,
        current_hour = current_hour ,
        current_minute = current_minute , 
        cantDay = cantDay ,
        
    )



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/horario")
def horario():
    return render_template("horario.html")


@app.route("/tareas")
def tareas():
    return render_template("tareas.html" ,)


@app.route("/sinfecha")
def sinfecha():
    return render_template("sinfecha.html" ,)


# @app.route("/lista")
# def lista():
#     return render_template("lista.html",)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
    # app.run(host='0.0.0.0', port=8000, debug=True)




