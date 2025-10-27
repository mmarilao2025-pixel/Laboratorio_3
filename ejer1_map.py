'''
Dada la lista [1,2,3,4,5], crear otra lista con cada elemento multiplicado por 10
usando map().
map ( funcion , iterable )
'''
lista = [1, 2, 3, 4, 5]
numero = list(map(lambda x : x*10, lista))
print(numero)