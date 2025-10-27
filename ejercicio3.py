'''
Crear una clase que genere los cuadrados de los números del 1 al 10 sin usar iter(),
pero proporcionando un método que devuelva la lista completa.
'''

class Cuadrados:
    def __init__(self):
        self.inicio=1
        self.fin=10
    def obtener_lista(self):
        return [n ** 2 for n in range(self.inicio, self.fin + 1)]

cuadrado = Cuadrados()
print(cuadrado.obtener_lista())