'''
Crear un generador de números impares del 1 al 20 usando yield en una clase e
iterarlo con un for.
'''
def numeros(lista):
    for num in lista:
        if num % 2 != 0:
            yield num
prueba = [1, 2, 3, 4, 5, 6, 7]
for n in numeros(prueba):
    print(n)