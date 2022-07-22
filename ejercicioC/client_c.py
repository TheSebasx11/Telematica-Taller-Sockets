# Importa las librerias del sockets
import pickle
import os
from socket import *
from prettytable import PrettyTable


def connection():
    servername = "localhost"
    # Se define el puerto por donde escucha el servidor
    serverport = 6000
    # Se establece la instancia del cliente sockets
    clienteSocket = socket(AF_INET, SOCK_STREAM)
    # Se establece la conexión con el servidor
    clienteSocket.connect((servername, serverport))
    return clienteSocket


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def send_message(option, data):
    msg = {
        'option': option,
        'data': data
    }

    # Se define la dirección ip a donde se va a apuntar al servidor
    # Se envia el mensaje al servidor con formato utf-8
    clienteSocket.send(pickle.dumps(msg))


table = PrettyTable()


def registro(apellidos, nombres, edad, estatura, color, med_busto, med_cintura, med_cadera):
    return {
        'Apellidos': apellidos,
        'Nombres': nombres,
        'Edad': edad,
        'Estatura': estatura,
        'Color de ojos': color,
        'Medida del busto': med_busto,
        'Medida de la cintura': med_cintura,
        'Medida de la cadera': med_cadera
    }


candidatas = [
    registro('Gomez', 'Ana', 20, 1.60, 'cafe', 36, 30, 34),
    registro('Perez', 'Sofia', 22, 1.70, 'verde', 38, 32, 36),
    registro('Gonzalez', 'Maria', 18, 1.75, 'azul', 40, 34, 38),
    registro('Fernandez', 'Daniela', 19, 1.65, 'negro', 42, 36, 40),
    registro('Lopez', 'Valentina', 21, 1.68, 'blanco', 44, 38, 42),
    registro('Lopez', 'Valentina', 21, 1.68, 'Azul', 60, 90, 60),
]


def imprimir_candidatas(candidatas):
    table.clear()
    table.field_names = ["Apellidos", "Nombres", "Edad", "Estatura", "Color de ojos",
                         "Medida del busto", "Medida de la cintura", "Medida de la cadera"]
    for candidata in candidatas:
        table.add_row([candidata["Apellidos"], candidata["Nombres"], candidata["Edad"], candidata["Estatura"], candidata["Color de ojos"],
                      candidata["Medida del busto"], candidata["Medida de la cintura"], candidata["Medida de la cadera"]])
#        print('-------------------------------------')
#        for campo, valor in candidata.items():
#            print(f'{campo}: {valor}')
#        print('-------------------------------------')
    print(table)


def recive_messaje():
    # Se obtiene mensaje cambiado por el servidor
    msg_modified = clienteSocket.recv(4096)
    # Guardamos el mensaje en una variable
    msg_modified = pickle.loads(msg_modified)
    # Se muestra el mensaje
    try:
        imprimir_candidatas(msg_modified['message'])
    except:
        print(msg_modified['message'])


def close():
    clienteSocket.close()


while 1:
    clienteSocket = connection()
    salir = False
    print('''
                1. Candidatas ordenadas por apellido
                2. Candidatas que tienen medidas perfectas
                3. Candidatas con ojos azules
                4. Un listado ordenado descendentemente por estatura
                5. Salir
                ''')
    opcion = int(input('Ingrese una opcion: '))
    match opcion:
        case 1:
            send_message(1, candidatas)
        case 2:
            send_message(2, candidatas)
        case 3:
            send_message(3, candidatas)
        case 4:
            send_message(4, candidatas)
        case 5:
            send_message(5, None)
            break
        case _:
            print('Option no valida!')
    recive_messaje()
    close()
