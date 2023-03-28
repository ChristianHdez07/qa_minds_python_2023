'''
Crear la siguiente lista:
	paises = [“México”, “Venezuela”, “Argentina”, “Brasil”, “Colombia”, “Panama”]
Una vez creada la lista, agregar el país Chile ordenarlos alfabéticamente.
Extra: Agregar una función para verificar si un país existe en la lista.
'''

def is_country_present(countries: list, target: str) -> bool:
    for country in countries:
        if country == target:
            return True
    return False

paises = ["México", "Venezuela", "Argentina", "Brasil", "Colombia", "Panama"]
paises.append("Chile")
paises.sort()
print(paises)
print(is_country_present(paises, "Venezuela"))
print(is_country_present(paises, "Uruguay"))