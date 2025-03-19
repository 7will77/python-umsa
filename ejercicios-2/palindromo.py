#Programa para evaluar y encontrar palabras palíndromas
#Que se leen igual de Derecha a Izquierda y de Izquierda a Derecha

palabra = input('Ingresa una palabra:')
cantidad_letras = len(palabra)
palindromo = True                           #Bandera para encontrar diferencias
for i in range(0,cantidad_letras //2):      #Barrido desde primera posicion has la mitad de la longitud de la palabra
    j= -i-1
    if palabra[i] != palabra[j]:            #Verifica diferencia en las letras
        palindromo = False
        break

if palindromo == True:
    print(f'La palabra: {palabra}, Si es un palíndromo')
else:
    print(f'La palabra: {palabra}, No es un palíndromo')

