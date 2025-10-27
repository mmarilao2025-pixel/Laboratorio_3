'''
Crear una lista con las primeras letras de las palabras de la lista ["python",
"java", Ç++", ruby"].
'''
palabras = ["python", "java", "C++", "ruby"]
primeras_letras = [p[0] for p in palabras]
print(primeras_letras)