import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

class CnC:
    def __init__():
        pass
    def server_loop(self):
        self.socket.bind(self.target,self.port)
        self.socket.listen(20)
        while True:
            client_socket, addr = self.socket.accpet()
            client_thread = threading.Thread(target=self.handler,args=(client_socket,))
            client_thread.start()
    def handle(self,client_socket):
        with self.Ccommand as c:
            if c == 'list':
                self.list()
            elif c == 'activate':
                self.activate()
            elif c == 'connect':
                self.connect()
            elif c == 'send':
                self.send()
            elif c == 'anhilate':
                self.anhilate()
            elif c == 'hashcracker':
                self.hashcracker()
            elif c == 'update':
                self.update()
    def list(self):
        pass
    def activate(self):
        pass
    def connect(self):
        pass
    def send(self):
        pass
    def anhilate(self):
        pass
    def hashcracker(self):
        pass
    def update(self):
        pass

def main():
    print('''
        <*> Welcome to the Co-ordinate
        <*> The fate of the Eldians lie on your hands
        <*> To begin type help to see tha available commands
    ''')

    while True:
        Ccommand = input("<*> ")