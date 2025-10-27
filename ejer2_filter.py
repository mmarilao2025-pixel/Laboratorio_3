'''
Filtrar las palabras que empiezan con “p” de la lista ["perro","gato","pato","hamster"].
'''
palabras = ["perro","gato","pato","hamster"]
p = list(filter(lambda x : x[0] == "p", palabras))
print(p)