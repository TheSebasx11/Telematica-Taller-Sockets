# Importa las librerias del sockets
from socket import *
import pickle
import os
# Se define la dirección ip a donde se va a apuntar al servidor
servername = "localhost"
# Se define el puerto por donde escucha el servidor
serverport = 6000

# preguntamos la cantidad de equipos que ingresaran al usuario
cantidad_equipos = int(
    input("Ingrese la cantidad de equipos que quiere participar: "))
nombres_equipos = []
# verificamos que este entre 10 y 20 equipos
if cantidad_equipos < 10 or cantidad_equipos > 20:
    print("La cantidad de equipos debe estar entre 10 y 20")
    exit()
else:
    # preguntamos por los nombres de los equipos
    for i in range(cantidad_equipos):
        nombres_equipos.append(
            input("Ingrese el nombre del equipo {}: ".format(i + 1)))

# Se establece la instancia del cliente sockets
clienteSocket = socket(AF_INET, SOCK_STREAM)
# Se establece la conexión con el servidor
clienteSocket.connect((servername, serverport))


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def send_message(msg):
    # Se define la dirección ip a donde se va a apuntar al servidor
    # Se envia el mensaje al servidor con formato utf-8
    clienteSocket.send(pickle.dumps(msg))


def show(msg_modified):
    datos = pickle.loads(msg_modified)
    if datos["data"] is not None:
        print("--> {}".format(datos["message"]))
        print("--> {}".format(datos["data"]))
    else:
        print("--> {}".format(datos["message"]))


def recive_message():
    # Se obtiene mensaje cambiado por el servidor
    msg_modified = clienteSocket.recv(4096)
    # Guardamos el mensaje en una variable
    
    # Se muestra el mensaje
    show(msg_modified)
    msg_modified = pickle.loads(msg_modified)
    if msg_modified['end'] is True:
        clienteSocket.send(pickle.dumps("-1"))
        print("Fin de la conexion")
        close()
        return True
    else:
        return False


def close():
    clienteSocket.close()
    print("Conexion cerrada")


# send_message(pickle.dumps(nombres_equipos_ejemplo))
send_message(nombres_equipos)
while 1:
    #msg_modified = clienteSocket.recv(4096)
    #msg_modified = pickle.loads(msg_modified)
    #print(msg_modified)
    if recive_message() is True:
        break
    else:
        continue


#
# Se solicita al cliente que escriba un mensaje
#msg=input("Escriba una palabra ")
#msg = pickle.dumps(msg)
# Se envia el mensaje al servidor con formato utf-8
# clienteSocket.send(msg)
# Se obtiene mensaje cambiado por el servidor
# msg_modified=clienteSocket.recv(1024)
#msg_modified = pickle.loads(msg_modified)
# se imprime el mensaje modificado por el servidor
#print("el mensaje cambiado es", msg_modified)
# Se cierra la conexión
# clienteSocket.close()
