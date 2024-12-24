from flask import Flask, render_template, request, redirect, flash, jsonify, session, make_response,  redirect, url_for
from datetime import datetime, date
# from flask_jwt import JWT, jwt_required, current_identity
# import uuid
# from functools import wraps
import hashlib
import base64
import controladores.controlador_horario as controlador_horario

app = Flask(__name__, template_folder='templates')


def generalPage(page):
    return "general_pages/"+page


def adminPage(page):
    return "admin_pages/"+page


@app.route("/")
def index():
    return render_template(generalPage("index.html"))



@app.route("/horario")
def horario():
    horarios = controlador_horario.obtener_horarios()
    return render_template(generalPage("horario.html") , horarios = horarios)














if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
