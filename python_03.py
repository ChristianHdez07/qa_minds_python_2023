nombre = input("¿Cual es su nombre?")
print(type(nombre))

edad_s = input("¿Cual es su edad?")
edad_i = int(edad_s)
print(type(edad_i))

ciudad = input("¿Cual es su ciudad de origen?")
print(type(ciudad))

estado_civil_s = input("¿Es casado?")
estado_civil_b = bool(estado_civil_s)
print(type(estado_civil_b))

numero1_s = input("¿Digite un numero entre 1-100?")
numero1_i = int(numero1_s)
print(type(numero1_i))

numero2_s = input("¿Digite un numero entre 100-200?")
numero2_i = int(numero2_s)
print(type(numero2_i))

division = numero1_i/numero2_i
print(division)

print(f"Mi nombre es {nombre}, mi edad es {edad_i}, soy de la ciudad de {ciudad} y mi resultado de la división es {division}")


