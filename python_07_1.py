'''
Imprime todos los números del 0 al 99, de dos en dos y que no sean múltiplos del 3
'''

for num in range(0, 100, 2):
    # Ignorar si es divisible entre 3
    if num % 3 == 0:
        continue
    # Imprimir numero
    print(num)