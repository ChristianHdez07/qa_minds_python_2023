"""
Dada una lista de Poker Planning
[0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100 ] indique:
- Cuantos de estos números son pares
- Cuantos son divisibles por el numero anterior y
que de un resultado entero mayor que cero. Ejemplo 2 / 1 = 2.
- Cual seria la sumatoria de todos los números.
"""

lista = [0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100]

pares = []
divisibles = []
suma = 0
for index, num in enumerate(lista):
    prev_num = lista[index - 1] if index > 0 else None  # Operador ternario
    if num % 2 == 0:
        pares.append(num)
    if prev_num and num % prev_num == 0:
        divisibles.append(num)
    suma += num

print(f"{len(pares)} son pares: {pares}")
print(f"{len(divisibles)} son divisibles: {divisibles}")
print(f"Suma: {suma}")