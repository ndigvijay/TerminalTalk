import socket
import threading

host = '0.0.0.0' 
port = 7976        

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames.pop(index)
                broadcast(f"{nickname} has left the chat! \n".encode('ascii'))
            break

def receive_clients():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        
        client.send("NICKNAME".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        
        print(f"Nickname: {nickname}")
        broadcast(f"{nickname} joined the chat! \n".encode('ascii'))
        client.send("Connected to the server! \n".encode('ascii'))
        
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is running...")
receive_clients()
