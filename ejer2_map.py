'''
Convertir la lista de grados Celsius [0, 10, 20, 30] a Fahrenheit usando map()
y una función lambda.
'''
lista = [0, 10, 20, 30]
numero = list(map(lambda x : (x * 1.8)+32, lista))
print(numero)