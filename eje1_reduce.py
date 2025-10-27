'''
Sumar todos los elementos de la lista [5,10,15,20] usando reduce().
from functools import reduce
reduce ( funcion , iterable )
'''
from functools import reduce
numeros = [5, 10, 15, 20]
suma= reduce(lambda x, y: x + y, numeros)
print(suma)