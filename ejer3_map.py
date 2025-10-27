'''
Dada la lista [üno","dos","tres"], crear otra lista con la longitud de cada palabra usando map().
'''
lista = ["uno", "dos", "tres"]
longitud = list(map(lambda x : len(x), lista))
print(longitud)