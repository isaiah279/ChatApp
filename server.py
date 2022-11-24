import socket
import time
import threading

HOST = '127.0.0.1'
PORT = 10319
server = socket.socket(socket.AF_INET)
server.bind((HOST, PORT))

server.listen()
clients = []

nicknames = []


# broadcast
def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        nickname.append(nickname)
        clients.append(client)
        print(f"Nickname of The client is {nickname}")
        broadcast(f'{nickname} connected to the server! \n'.encode('utf-8'))
        client.send("Connected to the serve successfully".encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("server running")
receive()

# receive


# handle
