# Puede abordar mi vuelo internacional a Japon:
# Boletos de avion
# Passaporte
# COVID (una de estas dos opciones):
#     TRES_VACUNAS_COVID
#     PRUEBA_PCR
'''
boleto_avion = True
passaporte = True
tres_vacunas_covid = False
prueba_pcr = False

if boleto_avion and passaporte and (tres_vacunas_covid or prueba_pcr):
    print("Abordar")
else:
    print("No abordar")
'''

'''
Escribe un script que dado la edad de una persona y su altura pueda determinar si la 
misma puede o no subirse en la montaña rusa “Push-Pull”, dado que se debe ser mayor a 
14 años y tener una altura no menor de 1,62. El script debe ser capaz de informar si 
puede o no subirse y en el caso de que no, porque razon (Si por edad, por tamaño u 
ambas) (editado) 
'''

# CONSTANS
AGE_LIMIT = 14
HEIGHT_LIMIT = 1.62

# USER INPUTS
age = input("age? ")
age = int(age)

height = input("height? ")
height = float(height)

#LOGIC
valid_age = age > AGE_LIMIT
valid_height = height > HEIGHT_LIMIT

if valid_age and valid_height:
    print("YES")
else:
    print(f"NO because valid age is {valid_age} and valid height is {valid_height}")



