'''
Concatenar todas las cadenas de la lista ["Hola", , "Mundo", ¡"] usando reduce().
'''
from functools import reduce
lista = ["Hola", "Mundo", "!"]
concatenar = reduce(lambda x, y: x+ " " +y, lista)
print(concatenar)
