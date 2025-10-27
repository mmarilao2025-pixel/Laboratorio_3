'''
Encontrar el número mayor de la lista [7,3,9,1,5] usando reduce().
'''
from functools import reduce
lista = [7, 3, 9, 1, 5]
mayor = reduce(lambda x, y: x if x>y else y, lista)
print(mayor)