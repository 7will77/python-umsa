## Sentencias encadenadas
numero = input('Introduzca un numero entero: ')
numero = int(numero)

if numero < 0:
    print(f'El numero {numero} es negativo')
elif numero == 0:
    print(f'El numero es igual a 0')

elif (numero >= 1) and (numero <= 10):                      ##Verifica que este entre 1 y 10
    print(f'El numero {numero} esta entre 1 y 10')

elif numero in range(11, 21):
    print(f'El numero {numero} esta entre 11 y 20')
else:
    print(f'El numero {numero} es mayor a 20')
