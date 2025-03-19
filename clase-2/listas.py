impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

'''
print(impares[:2])
print(impares[-2:])

indice=2
print(impares[:indice])
print(impares[-indice:])

print(impares[-7:-3])

# Union de listas
pares = [2, 4, 6, 8]
union = impares + pares
print (union)

#Tamaño del array
dimension = len(union)
print (dimension)

##FUNCIONES

impares.append(21)
print(impares)

## index    pop     remove  reverse

indice=impares.index(3)
print(indice)     #Muestra la posicion del elemento definido   

indice=impares.index(7)
valor=impares[indice]
print(f'indice: {indice}, valor: {valor}')


impares.pop(4)               #Elimina el elemento de la posicion 4
print(impares)

impares.remove(5)            #Elimina el elemento definido
print(impares)

impares.reverse()            #Invierte las posiciones de todos los elementos de la lista
print(impares)

impares.reverse()
print(impares)

numeros = [1, 5, 6, 2, 5, 8, 9, 10,]
indice = numeros.index (5,2,6)          #Buscar el 5 en el intervalo (2,6)
print(indice)

numeros = [1, 5, 6, 2, 5, 8, 9, 10,]
print(f''{numeros.index(5)} - {numeros.index(5,numeros.index(5)+1,-1)}'')

numeros.sort()                          #ordena los valores de manera ascendente de la lista
print(numeros)

#Alfanumerico
alfa_numerico=[1, 'a', 2, 'd', 6, 'z', 19, 0, 'a']
repeticion = alfa_numerico.count('a')
print(repeticion)

try :
    alfa_numerico.sort()        ## aqui hay un error
except:
    print('ocurrio un error, continua...')

print('Continua el codigo...')
print(alfa_numerico)
'''

valor = 'Hello_from_python'
print(valor[:5])

matriz = [
    [10,12,14,16,18],
    [20,22,24,26,28]
]

print(matriz[1][2])     #Muestra el valor 24


