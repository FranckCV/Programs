from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas
socketio = SocketIO(app, cors_allowed_origins="*")
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("get_data")
def send_data():
    # Datos de prueba para enviar al cliente
    test_data = [
        {"id": 1, "name": "AAaa", "score": 90},
        {"id": 2, "name": "Alice", "score": 85},
        {"id": 3, "name": "Bob", "score": 78},
    ]
    emit("update_table", {"data": test_data})  # Enviar datos al cliente

@socketio.on('connect')
def test_connect():
    print("Cliente conectado")




if __name__ == "__main__":
    socketio.run(app, debug=True)
