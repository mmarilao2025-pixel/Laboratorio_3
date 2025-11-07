'''
Crear una lista con los cuadrados de todos los números pares del 1 al 20.
[ expresion for elemento in iterable if condicion ]
'''
cuadrados = [i**2 for i in range(1, 21) if i % 2 == 0]
print(cuadrados)
