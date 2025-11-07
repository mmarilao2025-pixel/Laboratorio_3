'''
Crear un iterador que recorra los elementos de una lista de cadenas y devuelva
cada cadena en mayúsculas.
'''
class Mayuscula:
    def __init__(self, lista):
        self.lista = lista
        self.indice = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice < len(self.lista):
            valor = self.lista[self.indice].upper()
            self.indice += 1
            return valor
        else:
            raise StopIteration
        
palabras =["casa", "perro", "gato"]
for palabra in Mayuscula(palabras):
    print(palabra)
