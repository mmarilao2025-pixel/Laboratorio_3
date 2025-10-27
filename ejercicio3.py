'''
Filtrar los números mayores a 50 de la lista [10,60,30,80,50,100].
'''
lista = [10,60,30,80,50,100]
numero = list(filter(lambda x: x>50, lista))
print(numero)