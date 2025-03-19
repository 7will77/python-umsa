'''
indice 0, 1
indice 1, 3
...

'''
lista = [1,3,5,7,9,11,13,15]
#        0 1 2 3 4  5  6  7

dimension = len(lista)
print(dimension)
'''
for i in range(0, dimension):
    print(i, end=", ")

for i in range(2, dimension, 3):
    print(i, end=", ")

# Por indice
for i in range(0, len(lista)):
    print (f'indice: {i},  valor: {lista[i]}')
# Por elemento
for elemento in lista:
    print(f'valor: {elemento}')
'''