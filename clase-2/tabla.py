# Elaborar la tabla de multiplicar con un for

numero = input('Introduzca un numero: ')
numero = int(numero)
'''
for i in range(1, 11):
    resultado= numero * i
    print (f' {numero} x {i} = {resultado}')

#2

lista = range (1,10)  # [1,2,3,4,5,6,7,8,9,10]
for e in lista:
    print(f'{numero} x {lista.index(e)+1} = {e*numero}')
'''

for i in range(1, 11):
    resultado= numero * i
    print (f' {numero} x {i} = {resultado}')


