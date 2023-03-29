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

import random
from enum import Enum

#######################################################################################
# ABSTRACIONES DEL JUGADOR
#######################################################################################

class Estado(Enum):
    ACTIVO = 1
    INACTIVO = 2


class Jugador:
    def __init__(self, nombre, email, raza):
        self.nombre = nombre
        self.email = email
        self.raza = raza
        self.puntos = 0
        self.partidas = 0
        self.activo = True

    def __str__(self):
        return f"{self.nombre} ({self.raza}) - {self.puntos} puntos, {self.partidas} partidas"

    def perder_partida(self):
        self.puntos += 1
        self.partidas += 1
        self.activo = False

    def ganar_partida(self):
        self.puntos += 3
        self.partidas += 1


class Partida:
    def __init__(self, jugador1, jugador2):
        self.nombre = f"{jugador1.nombre} vs {jugador2.nombre}"
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.resultado = None

    def jugar_partida(self):
        if self.resultado is None:
            resultado = random.choice([self.jugador1, self.jugador2])
            if resultado == self.jugador1:
                self.jugador1.ganar_partida()
                self.jugador2.perder_partida()
            else:
                self.jugador2.ganar_partida()
                self.jugador1.perder_partida()
            self.resultado = resultado

    def __str__(self):
        return f"{self.nombre}: {self.resultado.nombre} gana"


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


def exportar_registros(jugadores):
    with open("Torneo_Starcraft.txt", "w") as f:
        for jugador in jugadores:
            f.write(str(jugador) + "\n")


#######################################################################################
# CONTROL PRINCIPAL
#######################################################################################
JUGADORES = []

MENU = {
    "alta": alta
}

# alta
OPTIONS = ' | '.join(MENU.keys())

for i in range(4):
    nombre = input(f"Ingrese el nombre del jugador {i + 1}: ")
    email = input(f"Ingrese el email del jugador {i + 1}: ")
    raza = input(f"Ingrese la raza del jugador {i + 1} (Terran, Zerg, Protoss): ")
    jugador = Jugador(nombre, email, raza)
    JUGADORES.append(jugador)

jugadores_activos = [jugador for jugador in JUGADORES if jugador.activo]
jugadores_mismo_numero_partidas = []
while len(jugadores_mismo_numero_partidas) != 2:
    jugador1, jugador2 = random.sample(jugadores_activos, 2)
    if jugador1.partidas == jugador2.partidas:
        jugadores_mismo_numero_partidas = [jugador1, jugador2]

partida = Partida(jugadores_mismo_numero_partidas[0], jugadores_mismo_numero_partidas[1])
partida.jugar_partida()
final = Partida(jugadores_mismo_numero_partidas[0], jugadores_mismo_numero_partidas[1])
final.jugar_partida()

exportar_registros(JUGADORES)
