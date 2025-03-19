#Programa para calcular el factorial de un numero

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

#Calculo del factorial del numero
factorial = numero
for i in range (numero-1, 0, -1):
    factorial *= i

print(f'El factorial de {numero} es: {factorial}')
