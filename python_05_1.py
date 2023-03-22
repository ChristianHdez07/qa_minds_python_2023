'''
Asigne el valor de la suma de los dos números a una variable llamada "suma".
Asigne el valor de la resta del segundo número menos el primer número a una variable llamada "resta".
Asigne el valor de la multiplicación de los dos números a una variable llamada "multiplicación".
Asigne el valor de la división entera del segundo número entre el primer número a una variable llamada "division_entera".
Asigne el valor del resto de la división del segundo número entre el primer número a una variable llamada "resto_division".
Imprime en pantalla el valor de cada una de las variables.
'''

num_a = input("Numero A: ")
num_b = input ("Numero B: ")
num_a = int(num_a)
num_b = int(num_b)

addition = num_a + num_b
subtraction = num_a - num_b
multiplication = num_a * num_b
division = num_a // num_b
rest_division = num_a % num_b

print(80 * "-")
print(f"Suma: {addition}")
print(f"Resta: {subtraction}")
print(f"Multiplacion: {multiplication}")
print(f"Division: {division}")
print(f"Resto division: {rest_division}")
print(80 * "-")

'''
Instrucciones:
Escribe un programa en Python que pida al usuario que introduzca dos números enteros y realice las siguientes comparaciones:
Comprueba si el primer número es mayor que el segundo número.
Comprueba si el primer número es menor que el segundo número.
Comprueba si el primer número es igual al segundo número.
Comprueba si el primer número es diferente al segundo número.
Para cada una de estas comparaciones, imprime en pantalla el resultado como un mensaje de texto que indique si es verdadero o falso.
'''

num_a = input("Numero A: ")
num_b = input("Numbero B: ")
num_a = int(num_a)
num_b = int(num_b)

print(f"Numero A > Numero B: {num_a > num_b}")
print(f"Numero A < Numero B: {num_a < num_b}")
print(f"Numero A == Numero B: {num_a == num_b}")
print(f"Numero A != Numero B: {num_a != num_b}")