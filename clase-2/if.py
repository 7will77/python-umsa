numero = input('Introduzca un numero entero: ')
try :
    numero = int(numero)
except:
    print('el valor debe ser un numero entero')
if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')