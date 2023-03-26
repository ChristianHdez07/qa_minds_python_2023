'''
EXTRA:
Escribe una función llamada "es_par" que tome un número entero como parámetro y
devuelva True si el número es par o False si el número es impar.
Luego, escribe un programa que pida al usuario que introduzca un número entero y
utilice la función "es_par" para determinar si el número es par o impar.
Imprime en pantalla un mensaje indicando si el número es par o impar.
'''

def es_par(var):
    if var % 2 == 0:
        return True
    else:
        return False

num = int(input("Numero: "))
print(f"ES PAR: {es_par(num)}")