'''
Extra: Define una función para convertir de grados Celsius a Fahrenheit,
pide al usuario que ingrese la temperatura en Celsius e imprima la conversión.
'''


def celsius_a_fahrenheit(temperatura_c):
    return (temperatura_c * 1.8) + 32

temperatura_f = float(input(f"Ingresa los grados celsius: "))
print(f'La conversion a grados Fahrenheit es: {celsius_a_fahrenheit(temperatura_f)}')