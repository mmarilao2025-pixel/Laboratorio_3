'''
Crear una lista con los números divisibles por 3 del 1 al 30.
'''
numeros = [i for i in range(1, 31) if i % 3 == 0]
print(numeros)