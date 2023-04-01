#import libs
import sys
import os
import socket
import pygame


pygame.init()

#define variables
PORT = int(sys.argv[1])
host = "localhost"


HOST = socket.gethostbyname(host)




#Connect to host at port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#try connecting to host
try:
    s.connect((HOST, PORT))
    print("Connected to server " + str(HOST))
    
except:
    print("ERROR: Could not connect to server")
    print("Quitting Program")
    quit()

    #store recived data in data_recived
decoded_data = s.recv(1024).decode()

player = int(decoded_data)
print("You are player " + str(decoded_data) )

running = True

while running:

    keys = pygame.key.get_pressed()
    print(keys)
    input()




    if (keys[pygame.K_a]):
        s.send(str.encode("a"))
        print("sendt")
        quit()





    if (keys[pygame.K_1]):
        quit()


print("Ended koop " + player)
data = input()
s.send(str.encode(data))
    

print(decoded_data)


