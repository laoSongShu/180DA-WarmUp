# Modified based on the example given in the tutorial of ECE 180DA

import socket
client = socket.socket()
client.connect(('Huaijins-MacBook-Air-4.local',8080))
#client.send('I am client\n')
client.send(('I am client\n').encode())
from_server = client.recv(4096).decode()
client.close()
print(from_server)

