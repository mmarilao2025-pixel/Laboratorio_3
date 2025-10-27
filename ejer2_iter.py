'''
Crear un generador de números impares del 1 al 20 usando yield en una clase e
iterarlo con un for.
'''
class Impares:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
    def __iter__ (self):
        for impar in range(self.inicio, self.fin + 1):
            if impar % 2 != 0:
                yield impar

for i in Impares(1, 20):
    print(i)
        