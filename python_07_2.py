'''
Dado un número aleatorio del 1 al 20 multiplicado por 2, imprime el valor del mismo.
Itera los números del 1 al 99, y en cuanto el número sea igual al número aleatorio
rompemos la iteración y muestre la suma de todos los números iterados hasta el momento.
'''

import random

# Generar numero random
rnd_num = random.randint(1, 20)
print(f"random number is: {rnd_num}")

# Agregar suma
result = 0

# Iterar
for num in range(1, 100):

    # Romper ciclo si num es igual a numero random
    if num == rnd_num:
        break

    # Sumar numero actual a resultado
    result += num
print(f"total sum: {result}")