"""
Define una tupla con los valores [1, 2, 3, 4, 5] e imprime el tamaño de la misma.
Luego dado un número aleatorio  entre el 1 y 5 recorrer la tupla e imprimí todos los números hasta que coincida el número generado.

"""
import random

tupla = (1, 2, 3, 4, 5)
rnd_num = random.randint(1, 5)

print(f"tamana de la tupla es {len(tupla)}")
for index, num in enumerate(tupla):
    if rnd_num == num:
        print(f"{rnd_num} se repite en el indice {index}")