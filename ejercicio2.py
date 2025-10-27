'''
Crear una función generadora que reciba una lista de números y devuelva solo los
números impares usando yield.
'''
def numeros(lista):
    for num in lista:
        if num % 2 != 0:
            yield num
prueba = [1, 2, 3, 4, 5, 6, 7]
for n in numeros(prueba):
    print(n)
