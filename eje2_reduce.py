'''
Multiplicar todos los elementos de la lista [2,3,4] usando reduce().
'''
from functools import reduce
numeros = [2, 3, 4]
mult = reduce(lambda x, y: x*y, numeros)
print(mult)