age = 10
print(age)
type(age)
print(type(age))

age = 45
age_hex = hex(age)
age_oct = oct(age)
age_bin = bin(age)
print(age_bin)
print(type(age_bin))

average = 9.1
print(average)
print(type(average))

name = "Christian Hernandez - Equipo 'Azul' "
print(name)
print(type(name))

name = str(10.5)
print(name)
print(type(name))

paragraph = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dol
ore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo cons
equat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
print(paragraph)
print(type(paragraph))

graduate = bool(7)
print(graduate)
print(type(graduate))

'''Instrucciones:
Cree una variable llamada "nombre" y asígnale su nombre como valor (ej. "Juan").
Cree una variable llamada "edad" y asígnale su edad como valor (ej. 30).
Cree una variable llamada "altura" y asígnale su altura en metros (ej. 1.75).
Cree una variable llamada "casado" y asígnale un valor booleano que indique si está casado o no (ej. False).
Cree una variable llamada "profesión" y asígnale su profesión como valor (ej. "Ingeniero").
Imprima en pantalla el valor de cada variable.
Verifique el tipo de dato de cada una de las variables e imprima en pantalla.
Extra:
Imprima en pantalla una frase que combine todos los valores de las variables anteriormente creadas (ej. "Mi nombre es Juan, tengo 30 años, mido 1.75 metros, no estoy casado y soy Ingeniero").
Nota: Para verificar el tipo de dato de una variable, se puede utilizar la función type().
'''

name = "Juan"
print(type(name))

age = 30
print(type(age))

height = 1.75
print(type(height))

wedded = False
print(type(wedded))

profesion =  "Ingeniero"
print(type(profesion))

print(f"Mi nombre es {name}, tengo {age} años, mido {height} metros, {wedded} casado y soy {profesion}")

a = 1
b = 2
c = 3
d = 4

# 1) Parentesis
# 2) Exponente
# 3) Division-Multiplicacion
# 4) Suma-Resta

result_1 = a + b + c + d
result_2 = a + b + c + d
print(result_1)
print(result_2)

'''
Instrucciones:
Cree tres variables numéricas, "a", "b", y "c", y asígnele un valor a cada una (ej. a = 10, b = 20, c = 30).
Realice las siguientes operaciones y asigne el resultado a una nueva variable:
(a + b) * c
 a + b * c
Imprima en pantalla el resultado de cada operación.
Explique la diferencia entre los dos resultados obtenidos y cómo la prioridad de los operadores influye en ellos.
'''

a = 10
b = 20
c = 30
result_1 = (a + b) * c
result_2 = a + b * c
print(result_1)
print(result_2)

name = "Alexis"
last_name = "Hernandez"
age = 28
print(f"Mi nombre es {name} {last_name}, mi edad es {age}")

'''
Instrucciones:
Cree tres variables: "name" (que almacene su nombre), "age" (que almacene su edad), y "city" (que almacene el nombre de la ciudad en la que vive).
Utilice formateo de cadenas para imprimir en pantalla la siguiente frase: "Mi nombre es [nombre], tengo [edad] años, y vivo en [ciudad]."
Utilice formateo de cadenas para crear una frase que incluya el valor de "pi" (3.14) y "e" (2.71). La frase debe decir: "Los valores de pi y e son aproximadamente 3.14 y 2.71, respectivamente."
Utilice el método de formato de cadenas f-strings para realizar las tareas 2 y 3.
Experimente con diferentes maneras de dar formato a las cadenas, como agregar tabulaciones y alineación.
'''

name = "Christian"
age = 28
city = "CDMX"
pi = 3.1416
e = 2.71
print(f"Mi nombre es {name}, tengo {age} años, y vivo en {city}.")
print(f"Los valores de pi y e son aproximadamente {pi} y {e}, respectivamente.")


