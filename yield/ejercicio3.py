'''
Crear una clase con un método __iter__() que use yield para generar los cuadrados 
de los números del 1 al 10.
'''
class Cuadrados:
    def __iter__(self):
        for i in range(1, 11):
            yield i ** 2

for numero in Cuadrados():
    print(numero)

