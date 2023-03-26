'''
Pide al usuario dos variables a = 12 y b = 34, crea funciones que permitan calcular
la suma, resta, multiplicación y división, como también el valor del módulo de b
entre a
'''

def sumar(num_a: int, num_b: int) -> int:
    '''Sumar dos numeros enteros
    :param num_a: Primer numero.
    :param num_b: Segundo numero.
    :return: Resultado de sumar primer numero + segundo numero
    '''
    print(f"OPERACION SUMA: {num_a} + {num_b}")
    return num_a + num_b

def restar(num_a: int, num_b: int) -> int:
    '''Restar dos numeros enteros
    :param num_a: Primer numero.
    :param num_b: Segundo numero.
    :return: Resultado de restar primer numero - segundo numero
    '''
    print(f"OPERACION RESTA: {num_a} - {num_b}")
    return num_a - num_b

def multiplicar(num_a: int, num_b: int) -> int:
    '''Multiplicar dos numeros enteros
    :param num_a: Primer numero.
    :param num_b: Segundo numero.
    :return: Resultado de multiplicar primer numero - segundo numero
    '''
    print(f"OPERACION MULTIPLICACION: {num_a} * {num_b}")
    return num_a * num_b

def dividir(num_a: int, num_b: int) -> int:
    '''Dividir dos numeros enteros
    :param num_a: Primer numero.
    :param num_b: Segundo numero.
    :return: Resultado de dividir primer numero / segundo numero
    '''
    print(f"OPERACION DIVISION: {num_a} / {num_b}")
    return num_a / num_b

def modulo(num_a: int, num_b: int) -> int:
    '''Modulo de numeros enteros
    :param num_a: Primer numero.
    :param num_b: Segundo numero.
    :return: Resultado de modulo primer numero % segundo numero
    '''
    print(f"OPERACION MODULO: {num_a} % {num_b}")
    return num_a % num_b

def convertir_entero(var):
    ''' Convertir una variable a entero
    :param var:
    :return:
    '''
    return int(var)

primer_numero = input("Numero A: ")
segundo_numero = input("Numero B: ")
primer_numero = int(primer_numero)
segundo_numero = int(segundo_numero)

print(f"Resultado suma: {sumar(primer_numero, segundo_numero)}")
print(f"Resultado resta: {restar(primer_numero, segundo_numero)}")
print(f"Resultado multiplicacion: {multiplicar(primer_numero, segundo_numero)}")
print(f"Resultado division: {dividir(primer_numero, segundo_numero)}")
print(f"Resultado modulo: {modulo(primer_numero, segundo_numero)}")