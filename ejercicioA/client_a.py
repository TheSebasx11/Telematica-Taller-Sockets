import pickle
#Importa las librerias del sockets
from socket import*
from os import system
import sys
import threading
from elements import Elemento

#Se define la dirección ip a donde se va a apuntar al servidor
servername ="192.168.1.7"
#Se define el puerto por donde escucha el servidor
serverport=12000
#Se establece la instancia del cliente sockets
clienteSocket= socket(AF_INET,SOCK_STREAM)
#Se establece la conexión con el servidor
clienteSocket.connect((servername,serverport))

def InsertarEstudiante():
    system("cls")
    print("Inserte un nuevo estudiante")
    
    cedula=input("Por favor ingrese la cedula: ")
    nombre=input("Por favor ingrese el nombre: ")
    apellidos=input("Por favor ingrese los apellidos: ")
    nota1=input("Por favor ingrese la nota1: ")
    nota2=input("Por favor ingrese la nota2: ")
    nota3=input("Por favor ingrese la nota3: ")
    nota4=input("Por favor ingrese la nota4: ")

    return Elemento(cedula, nombre, apellidos, nota1, nota2, nota3, nota4)

def menu():
    while True:# system("cls")
        
        print("Menu")
        print("1) Listar por apellidos")
        print("2) Insertar nuevo estudiante")
        print("3) Ver definitiva del estudiante")
        print("4) Visualizar contenido")
        print("5) Salir del programa")

        eleccion = input("Digite lo que quiere hacer: ")
        eleccion = eleccion.strip()
        clienteSocket.send(pickle.dumps(eleccion))
        if (eleccion == "1"):
            msg=clienteSocket.recv(1024)
            print(pickle.loads(msg))
        elif (eleccion == "2"):
            student = InsertarEstudiante()
            dump = pickle.dumps(student)
            clienteSocket.send(dump)
        elif (eleccion == "3"):
            msg=clienteSocket.recv(1024)
            print(pickle.loads(msg))
        elif (eleccion == "4"):
            msg=clienteSocket.recv(1024)
            print(pickle.loads(msg))
        elif (eleccion == "5"):
            print("Saliendo del servidor")
            clienteSocket.close()
            sys.exit()
        else:
            print("Opción invalida, por favor intentelo con un dato antes mencionado")

menuThread = threading.Thread(target=menu)
menuThread.start()