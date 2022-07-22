#Se importan todas las librerias de sockets
from socket import*
import pickle
import sys
import random
import time

def campeones(nombres_equipos, socket):
    random.shuffle(nombres_equipos)  # Mezclo los nombres de los equipos
    socket.send(pickle.dumps(
        {"message": "Los equipos en el campeonato son: ", "data": nombres_equipos, "end": False}
    ))  # Envio los nombres de los equipos
    time.sleep(1.5)

    socket.send(pickle.dumps(
        {"message": "\nSe formarán los siguientes grupos:  \n", "data": None, "end": False}
    ))
    lenn = int(len(nombres_equipos)/2)
    grupo1 = nombres_equipos[:lenn]  # Se forma el primer grupo con los 10 primeros elementos del vector
    grupo2 = nombres_equipos[lenn:]  # Se forma el segundo grupo con los 10 últimos elementos del vector
    time.sleep(1.5)

    socket.send(pickle.dumps(
        {"message": "Grupo 1: ", "data": grupo1, "end": False}
    ))
    time.sleep(1.5)

    socket.send(pickle.dumps(
        {"message": "Grupo 2: ", "data": grupo2, "end": False}
    ))
    time.sleep(1.5)

    socket.send(pickle.dumps(
        {"message": "\nLos siguientes equipos pasan a la siguiente ronda: \n", "data": None, "end": False}
    ))
    time.sleep(1.5)

    random.shuffle(grupo1)  # Mezclo el vector de nombres de los equipos del primer grupo
    random.shuffle(grupo2)  # Mezclo el vector de nombres de los equipos del segundo grupo

    socket.send(pickle.dumps(
        {"message": "Grupo 1: ", "data": grupo1[:2], "end": False}
    ))
    time.sleep(1.5)

    socket.send(pickle.dumps(
        {"message": "Grupo 2: ", "data": grupo2[:2], "end": False}
    ))
    time.sleep(1.5)

    socket.send(pickle.dumps(
        {"message": "\nLos siguientes equipos pasan a la final: \n", "data": None, "end": False}
    ))
    time.sleep(1.5)

    final = grupo1[:2] + grupo2[:2]  # Se forma el vector final con los 4 elementos de los dos grupos

    random.shuffle(final)  # Mezclo los nombres de los equipos de la final

    socket.send(pickle.dumps(
        {"message": "Final: ", "data": final[:2], "end": False}
    ))
    time.sleep(1.5)

    socket.send(pickle.dumps(
        {"message": "\nEl siguiente equipo es el campeón: \n", "data": None, "end": False}
    ))
    time.sleep(1.5)

    campeon = final[:1]  # Se forma el vector campeon con el primer elemento del vector final

    socket.send(pickle.dumps(
        {"message": "Campeón: ", "data": campeon, "end": True}
    ))
    
    serverSocket.close()
    sys.exit()



#puerto por donde escuchará el servidor
serverPort =6000
#Se instancia el servidor TCP
serverSocket = socket(AF_INET,SOCK_STREAM)
#Se define el puerto del servidor
serverSocket.bind(("localhost",serverPort))
#Servidor en modo escucha
serverSocket.listen(1)
print("El servidor esta listo para recibir peticiones:")
while 1:
    #Se extrae la información del puerto y la dirección ip del servidor
    conSocket, addr = serverSocket.accept()
    print("Recibiendo mensajes desde el cliente", addr)
    #Obtiene la información extraida del cliente
    msg = conSocket.recv(4096)
    n = pickle.loads(msg)
    print("Mensaje recibido: ", n)
    if n == "-1":
        serverSocket.close()
        sys.exit()
    
    campeones(n, conSocket)
    