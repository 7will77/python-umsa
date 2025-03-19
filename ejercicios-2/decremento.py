#Programa que pide un numero, valida que sea un entero mayor a Cero
#Muestra la cuenta hacia atras del numero en pantalla.
#Introduce un numero entero mayor a Cero: 8
#8, 7, 6, 5, 4, 3, 2, 1, 0,

#Validacion de que se trate de un numero entero mayor a Cero
while True:
    numero = input ('Introduce un numero entero mayor a Cero:')
    try:
        numero = int(numero)
        if numero > 0:
            break
        else:
            print('El número ingresado no es mayor a Cero')
    except ValueError:
        print('Solo se permiten numeros mayores a cero')

#Muestra en pantalla el decremento del numero ingresado
for i in range(numero, -1, -1):
        print(f'{i},', end=' ')