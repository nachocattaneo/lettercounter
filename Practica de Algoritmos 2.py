#Vamos a realizar en codigo lo que hicimos en pseudocodigo

from itertools import count


palabra_ingresada = input("Por favor ingrese la palabra cuyas letras hay que contar: ")

cant_letras = len(palabra_ingresada)

print(f"La palabra {palabra_ingresada} tiene {cant_letras} letras")