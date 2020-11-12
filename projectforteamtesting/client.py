'''

# Modified based on https://flask-socketio.readthedocs.io/en/latest/
# Also from https://medium.com/@rohanjdev/how-to-use-socket-io-with-flask-heroku-af9909e2e9a4

import socketio
sio = socketio.AsyncClient()

#@sio.event
#async def message(data):
#    print('I received a message!'+data)

@sio.on('remote_state')
def depth(data):
    print('print message id: ', data['id'])
    print('print message contents: ', data['message'])

@sio.event
async def connect():
    print("I'm connected!")

@sio.event
async def connect_error():
    print("The connection failed!")

@sio.event
async def disconnect():
    print("I'm disconnected!")

async def startConnection():
    await sio.connect('https://projectforteamtesting.herokuapp.com', transports=['websocket'])

startConnection()

async def mainFunc():
    for index in range(10):
        data = {
            "id": 0,
            "message": ""
        }
        data["id"] = input("What channel do you want to put your message? ")
        data["message"] = input("What message do you want to send?")
        await sio.emit('state',data)

mainFunc()

sio.wait()
'''


import socketio
sio = socketio.Client()

#@sio.event
#def connect():
#print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

@sio.on('remote_state')
def printValue(data):
    print('print message id: ', data['id'])
    print('print message contents: ', data['message'])
    print("")

@sio.on('receive')
def on_receive(data):
    print("")
    print(data)

sio.connect('https://projectforteamtesting.herokuapp.com', transports=['websocket'])
#sio.connect('http://0.0.0.0:5000', transports=['websocket'])

'''
for index in range(10):
    data = {
    "id": 0,
    "username": ""
    "message": ""
    }
    
    data["id"] = input("What channel do you want to put your message? ")
    data["username"] = input("What is your name? ")
    data["message"] = input("What message do you want to send? ")
    sio.emit('join',data)
    print("")
'''

data = {
    "id": 0,
    "username": "",
    "message": ""
}
data["id"] = input("What channel do you want to put your message? ")
data["username"] = input("What is your name? ")
sio.emit('join',data)
print("")

'''
for index in range(10):
    result = input("Do you want to leave?")
    if result == "yes":
        sio.emit("leave",data)
        break
    data["message"] = input("What do you want to say? ")
    sio.emit("messageMe", data)
    print("")
'''

while True:
    result = input("Say something: (leave)")
    if result == "leave":
        sio.emit("leave",data)
        break
    data["message"] = result
    sio.emit("messageMe", data)
    print("")
#sio.wait()


