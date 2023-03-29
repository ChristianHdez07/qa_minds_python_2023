'''
QA Minds Lab con motivo de finalizar el módulo de Introducción a Python realizará
un torneo de Starcrafts2. Para ello requiere de un sistema que permita gestionar
el torneo.

En este sentido el sistema debe contar con la posibilidad de crear jugadores, los
cuales tendrán un nombre, un email, puntos ganados y una Raza con la que jugarán, el
cual pueden ser: Terran, Zerg o Protoss.

Los jugadores también tendrán un estado el cual puede ser Activo o Inactivo, el cual
permitirá poder asociarlo a nuevas partidas o no.

Los jugadores también tendrán un contador de partidas.
Los jugadores también tendrán un contador de puntos.
'''

from enum import Enum

#######################################################################################
# ABSTRACIONES DEL JUGADOR
#######################################################################################

class Estado(Enum):
    ACTIVO = 1
    INACTIVO = 2

class Jugador:
    def __init__(self, nombre: str, email: str, raza: str, estado: Estado):
        self.__nombre = nombre
        self.__email = email
        self.__raza = raza
        self.__estado = estado

    def obtener_nombre(self):
        return self.__nombre

    def obtener_apellido(self):
        return self.__email

    def obtener_mail(self):
        return self.__raza

    def obtener_estado(self):
        return self.__estado

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"(nombre={self.__nombre}, email={self.__email}, raza={self.__raza} estado={self.__estado})"


#######################################################################################
# ACCIONES DEL SISTEMA
#######################################################################################
def alta():
    imprimir_header("ALTA")
    nombre = input("nombre?")
    email = input("mail?")
    raza = input("raza?")
    estado = input("estado?")
    jugador = Jugador(nombre, email, raza, Estado[estado])
    JUGADORES.append(jugador)
    print(f"Jugador registrado: {jugador}")

def imprimir_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")


#######################################################################################
# CONTROL PRINCIPAL
#######################################################################################
JUGADORES = []

MENU = {
    "alta": alta
}

# alta | salir
OPTIONS = ' | '.join(MENU.keys())

while True:
    action = input(f"Dar de alta jugador -> {OPTIONS}\n")
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Salir del sistema: {action}")