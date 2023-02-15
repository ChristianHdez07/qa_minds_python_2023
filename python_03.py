nombre = input("¿Cual es su nombre?")
print(type(nombre))

edad = input("¿Cual es su edad?")
edad = int(edad)
print(type(edad))

ciudad = input("¿Cual es su ciudad de origen?")
print(type(ciudad))

estado_civil = input("¿Es casado?")
estado_civil = bool(estado_civil)
print(type(estado_civil))

numeroa= input("¿Digite un numero entre 1-100?")
numeroa = int(numeroa)
print(type(numeroa))

numerob = input("¿Digite un numero entre 100-200?")
numerob = int(numerob)
print(type(numerob))

division = numerob/numerob
print(division)

print(f"Mi nombre es {nombre}, mi edad es {edad}, soy de la ciudad de {ciudad} y mi resultado de la división es {division}")


