import socket
import threading
import os
from dotenv import load_dotenv

load_dotenv()
port = int(os.getenv('PORT'))
ngrok_host = os.getenv('NGROK_HOST')  

def print_welcome_message(nickname):
    welcome_message = f"""
    {'=' * 50}
    {' ' * 10}Welcome to TerminalTalk :), {nickname.upper()}! 🎉
    {'=' * 50}
    """
    print(welcome_message)

nickname = input("Choose your nickname: ").strip() 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if not port or not ngrok_host:
    print("Error: Please set the PORT and NGROK_HOST in the .env file.")
    exit(1)

client.connect((ngrok_host, port))  

print_welcome_message(nickname)

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception as e:
            print(f"An error occurred: {e}. Disconnected from server.")
            client.close()
            break

def send_messages():
    while True:
        try:
            message = f'{nickname}: {input("")}'
            client.send(message.encode('ascii'))
        except Exception as e:
            print(f"Failed to send message: {e}.")
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
