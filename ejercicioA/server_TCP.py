# Se importan todas las librerias de sockets
import pickle
from socket import *

from os import system
import sys
import threading
from elements import Elemento
# Esto lo usaremos para guardar y mostrar los datos de manera ordenada y facil
from prettytable import PrettyTable
# puerto por donde escuchará el servidor
serverPort = 12000
# Se instancia el servidor TCP
serverSocket = socket(AF_INET, SOCK_STREAM)
# Se define el puerto del servidor
serverSocket.bind(("192.168.1.7", serverPort))

table = PrettyTable()
tablaDef = PrettyTable()
# Configuramos las columnas

#Seteamos los campos

table.field_names = ["Cedula", "Nombre", "Apellidos", "nota1", "nota2", "nota3", "nota4"]
Elements = []

system("cls")

def Definitivas():
    tablaDef.clear()
    tablaDef.field_names = ["Cedula", "Nombre", "Apellidos", "Definitiva"]
    for y in Elements:
        tablaDef.add_row([y.cedula, y.nombre, y.apellidos, y.Definitiva()])
    return tablaDef.get_string()

def MostrarVector():
    return table.get_string()

def ListaApellidos():
    table.sortby = "Apellidos"
    return table.get_string()

def InsertarEstudiante(student):
    Elements.append(student)
    table.add_row([student.cedula, student.nombre, student.apellidos, student.nota1, student.nota2, student.nota3, student.nota4])

def listenClients():
    # Servidor en modo escucha
    serverSocket.listen()
    print("El servidor esta listo para recibir peticiones:")
    # Se extrae la información del puerto y la dirección ip del servidor
    conSocket, addr = serverSocket.accept()
    
    while True:
        
        print("Recibiendo mensajes desde el cliente", addr)
        eleccion = conSocket.recv(1024)
        eleccion = pickle.loads(eleccion.strip())
        print(eleccion)
        if (eleccion == "1"):
            conSocket.send(pickle.dumps(ListaApellidos()))
        elif (eleccion == "2"):
            student = conSocket.recv(1024)
            studentLoaded = pickle.loads(student)
            InsertarEstudiante(studentLoaded)
        elif (eleccion == "3"):
            conSocket.send(pickle.dumps(Definitivas()))
        elif (eleccion == "4"):
            conSocket.send(pickle.dumps(MostrarVector()))
        elif (eleccion == "5"):
            print("Saliendo del servidor")
            serverSocket.close()
            sys.exit()
        else:
            print("Opción invalida, por favor intentelo con un dato antes mencionado")


# Configuramos el hilo del servidor
serverThread = threading.Thread(target=listenClients)

# Comenzamos los hilos
serverThread.start()

