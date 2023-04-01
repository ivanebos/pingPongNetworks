#Import Libs
import socket
import sys
import os
from _thread import *
import pygame

pygame.init()


#concurrent clients function
def client(connection, player):
    data = str(player)

    connection.send(str.encode(data))

    decoded_data = connection.recv(1024).decode()
    run = True
    while run:
        recived = connection.recv(1024).decode()
        if (recived == "a"):
            print("a")
        else:
            quit()

    
        
    connection.close()

# define the host and port
# server name is localhost ip
host = 'localhost'
port = int(sys.argv[1])



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

running = True


def connect_clients(number):
    print("Waiting for a player " + str(number) + " to connect")

    #client connect
    conn, address = server.accept()

    start_new_thread(client, (conn, number,))


    print("Player "+str(number)+" conneted")


#server infinite loop
while running:


    print("here")
    connect_clients(1)

    connect_clients(2)


    
    if ():
        running = False


