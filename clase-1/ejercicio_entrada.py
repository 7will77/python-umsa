'''
Crear un programa que asigne una
bonificacion al saldo de la persona
la bonificacion es de 125,6
y se debe pedir el nombre de la persona y su saldo actual
# Tu saldo total es: #####

nombre = input("Ingresa tu nombre: ")
saldo = input("Ingresa tu saldo: ")
saldo = int(saldo)
saldototal = saldo + 125.6

print(f'{nombre}:\n Tu saldo total es: {saldototal}')
'''

bonificacion = 125.6
nombre = input("Ingresa tu nombre: ")
saldo = input("Ingresa tu saldo: ")
# saldo = int(saldo)
saldo = float(saldo)
total = saldo + bonificacion
print(f'{nombre}:\nTu saldo es: {total}')

