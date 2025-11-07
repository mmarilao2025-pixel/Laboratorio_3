'''
Crear un contador del 10 al 15 usando iter() y recorrerlo con next().
'''

class Contador :
    def __init__ (self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __iter__ (self):
        return self 
    
    def __next__ (self):
        if self.inicio <= self.fin:
            valor = self.inicio
            self.inicio += 1
            return valor
        else :
            raise StopIteration

contador = Contador(10, 15)
it = iter(contador)

try:
    while True:
        print(next(it))
except StopIteration:
    pass

