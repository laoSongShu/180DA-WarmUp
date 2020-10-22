# Modified based on the example given in the tutorial of ECE 180DA

import socket
serv = socket.socket()
HOST = 'Huaijins-MacBook-Air-4.local'
PORT = 8080
serv.bind((HOST,PORT))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096).decode()
        if not data: break
        from_client += data
        print(from_client)
        conn.send(("I am SERVER\n").encode())
    conn.close()
    print('client disconnected')
