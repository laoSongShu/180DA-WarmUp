# Modified based on https://flask-socketio.readthedocs.io/en/latest/
# Also from https://medium.com/@rohanjdev/how-to-use-socket-io-with-flask-heroku-af9909e2e9a4

from flask import Flask, render_template, make_response, redirect
from flask_socketio import SocketIO, send, emit
import os
from flask_socketio import join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app, logging=True)
socketio.init_app(app, cors_allowed_origins="*")
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("state")
def handleMessage(data):
    emit("remote_state", data, broadcast=True)

@socketio.on("join")
def on_join(data):
    room = data["id"]
    username = data["username"]
    join_room(room)
    emit("receive", username + " has enter the room" + room + ". ", room=room)

@socketio.on("leave")
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit("receive", username + ' has left the room.', room=room)

@socketio.on("messageMe")
def on_messageMe(data):
    emit("receive", data["username"] + " send a message: " + data["message"] + ". ", room = data["id"])

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=port)
