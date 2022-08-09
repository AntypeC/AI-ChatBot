import socket
import threading
from sys import platform
import os

HOST = '127.0.0.1'
PORT = 9090

class User:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.connect()
        self.clear_console()

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def connect(self):
        print(f"Connecting to {self.host}:{self.port}. Please wait...")
        try:
            self.sock.connect((self.host, self.port))
        except Exception as e:
            print(e)
            self.connect()

    def write(self):
        message = input(f"{socket.gethostname()} >> ").encode('utf-8')
        self.sock.send(message)

    def clear_console(self):
        if platform == "linux" or platform == "darwin":
            os.system('clear')
        else:
            os.system('powershell "clear"')

    def stop(self):
        self.sock.close()
        quit()

    def receive(self):
        while True:
            try: 
                message = self.sock.recv(1024).decode('utf-8')
                print(message)
                self.write()
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.stop()

client = User(HOST, PORT)