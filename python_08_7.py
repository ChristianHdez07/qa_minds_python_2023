"""
Crear un metodo para validar si una lista es un palindromo.

Por ejemplo:
lista = ["a", "c", "a", "v", "a", "r", "a", "c", "a", "r", "a", "v", "a", "c", "a"]

is_palindrome(lista) # Debe regresar true
"""
lista = ["a", "c", "a", "v", "a", "r", "a", "c", "a", "r", "a", "v", "a", "c", "a"]


def is_palindrome(lst: list) -> bool:
    reverse = lst[::-1]
    for index, _ in enumerate(lst):
        if lst[index] != reverse[index]:
            return False
    else:
        return True

print(is_palindrome(lista))