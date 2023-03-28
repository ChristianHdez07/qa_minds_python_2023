class Car():
    INSTANCE_COUNTER = 0

    def __init__(self, color: str, propietario: str):
        self.__color = color
        self.__numero_puertas = 4
        self.__llantas = 4
        self.__propietario = propietario
        self.__status = "APAGADO"
        Car.INSTANCE_COUNTER += 1

    def paint(self, color):
        if color is not None and color in ["Rojo", "Amarillo", "Azul"]:
            self.__color = color
        else:
            print(f"WARNING - Invalid Color {color}")

    def __str__(self):
        return f"Color={self.__color}, Numero Llantes={self.__llantas}"


red_car = Car("Rojo", "prop1")
print(str(red_car))