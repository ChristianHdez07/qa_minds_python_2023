"""
Define una lista con los valores [1, 2, 3, 4, 5] e imprime el tamaño de la misma.
Luego genera un número aleatorio  entre el 1 y 10, agrega el nuevo valor en la lista.

Imprime cuantas veces se encuentra el valor nuevo en la lista.
"""

import random

lista = [1, 2, 3, 4, 5]

print(f"El tamaño de la lista es: {len(lista)}")

rnd_num = random.randint(1,10)
print(f"Se va a agregar {rnd_num} a la lista")
lista.append(rnd_num)

print(f"Lista final {lista}")
print(f"El numero {rnd_num} aparece {lista.count(rnd_num)} veces")