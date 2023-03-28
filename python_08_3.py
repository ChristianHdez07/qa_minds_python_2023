"""
Define una lista de 9 registros con valores aleatorios del 1 al 9.

Recorre la lista en búsqueda de números repetidos.
Si existe un número repetido cancela el proceso y
manda un mensaje indicando cuál número está repetido.
De lo contrario, muestra un mensaje que indique que no
existen números repetidos.
"""
import random

# Generar lista
lista = []
for _ in range(9):
    rnd_num = random.randint(1,9)
    lista.append(rnd_num)

print(f"Mi lista es: {lista}")

# Buscar numeros
for num in lista:
    if lista.count(num) > 1:
        print(f"El numero {num} se repite, {lista.count(num)} veces")
        break
else:
    print("No tiene numeros repetidos")