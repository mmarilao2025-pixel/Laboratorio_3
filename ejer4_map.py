'''
Dada la lista [1,2,3,4,5], crear otra lista con el cuadrado de cada número usando
map().
'''
lista = [1, 2, 3, 4, 5]
cuadrado = list(map(lambda x : x **2, lista))
print(cuadrado)