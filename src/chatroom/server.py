import socket
import sys
import os
import time
sys.path.insert(0, r"C:\Users\Antype Cryptous\Desktop\dev\AI-ChatBot")
from app import ChatBot

HOST = "0.0.0.0"
PORT = 9090

def clear_console():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system('clear')
    else:
        os.system('powershell "clear"')

clear_console()
print("Loading up the server...")

ai = ChatBot(name="Dev")
clear_console()

print("Loading up the server... Done")
time.sleep(1)
clear_console()

def encode_msg(feed=''):
    return feed.encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"{addr} joined the server!")
        conn.sendall(encode_msg(f"{ai.name} >> {ai.welcome_prompt(ai.name)}"))
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                print(f"{addr} left the server!")
                break
            r = ai.generate_response(data)
            conn.sendall(encode_msg(f"{ai.name} >> {r}"))
