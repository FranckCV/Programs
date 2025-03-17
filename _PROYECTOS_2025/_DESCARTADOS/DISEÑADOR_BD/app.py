from flask import Flask, render_template, request, redirect, flash, jsonify, session, make_response,  redirect, url_for
# from flask_jwt import JWT, jwt_required, current_identity
# import uuid
# from functools import wraps
import hashlib
import base64
from datetime import datetime, date
from flask_socketio import SocketIO, emit


app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app)


@app.route("/")
@app.route("/index") 
def index():
    return render_template("general_pages/index.html")


@app.route('/dashboard') 
def dashboard():
    return render_template("general_pages/dashboard.html")


@socketio.on('update_canvas')
def update_canvas(data):
    emit('update_canvas', data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
