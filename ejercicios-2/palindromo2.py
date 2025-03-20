#Programa para verificar si una palabra es palíndromo
#Palíndromo es la palabra leida de Izquierda a Derecha identica que si la leemos de Izquierda a Derecha

palabra = input('Ingrese una palabra en minusculas: ')
palabra_der = list(palabra)
palabra_inv = list(palabra)
palabra_inv.reverse()

if palabra_der == palabra_inv:
    print (f'La palabra {palabra}, es un Palíndromo')

else:
    print (f'La palabra {palabra}, no es un Palíndromo')