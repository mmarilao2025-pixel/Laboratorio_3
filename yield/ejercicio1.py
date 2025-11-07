'''
Crear una función generadora que devuelva los primeros 10 números pares usando
yield y recorrerla con un for
'''
def devolver():
    for i in range (20):
        if i % 2 == 0:
            yield i
for numero in devolver():
    print(numero)

