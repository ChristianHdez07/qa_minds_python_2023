"""
Dada una tupla de distribución de puntos para la Fórmula 1 (25, 18, 15, 12, 10, 8, 6, 4, 2, 1 ) indique:
Cuántos de estos números son pares
Cuantos puntos se le entregan a los tres primeros.
Cual seria la sumatoria de todos los números.
"""

tupla = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)
pares = []
suma_total = 0
primeros_tres = 0
for index, num in enumerate(tupla):
    if num % 2 == 0:
        pares.append(num)

    if index <= 2:
        primeros_tres += num

    suma_total += num
print(f"Numeros pares: {pares}")
print(f"Suma total: {suma_total}")
print(f"Suma primeros tres: {primeros_tres}")