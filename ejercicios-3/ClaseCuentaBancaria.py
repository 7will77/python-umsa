import datetime

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []  # Lista de tuplas: (fecha, tipo, monto, saldo)

    def depositar(self, monto):
        # Completar lo siguiente: 
        # 1. actualizar saldo 
        # 2. añadir movimiento de deposito (fecha, tipo, monto, saldo)
        # 3. Mostrar mensaje de depósito exitoso

        self.monto = monto
        self.saldo += self.monto 
        
        fecha = '28-03-2025'
        self.fecha = fecha
        tipo = 'Depósito'
        self.tipo = tipo
        self.movimientos.append((self.fecha, self.tipo, self.monto, self.saldo))
        
        print('Deposito realizado exitosamente')
        print(f'Fecha :{self.fecha}')
        print(f'Titular de la cuenta: {self.titular}')
        print(f'Operación Realizada: {self.tipo}')
        print(f'Saldo : {self.saldo}')
        print(f'Saldo : {self.movimientos}')

    def retirar(self, monto):
        # Completar lo siguiente: 
        # 1. Validar saldo, y si es insuficiente mostrar mensaje
        # 2. Actualizar saldo
        # 3. Añadir movimiento de retiro (fecha, tipo, monto, saldo) 
        # 4. Mostrar mensaje de retiro exitoso
        self.monto = monto
        fecha = '28-03-2025'
        self.fecha = fecha
        tipo = 'Retiro'
        self.tipo = tipo

        if self.monto > self.saldo:
            print(f'\nNo cuenta con saldo suficiente, su saldo es de: {self.saldo}')
        else:
            self.saldo -= self.monto
            self.movimientos.append((self.fecha, self.tipo, self.monto, self.saldo))
            print('\nRetiro realizado exitosamente')
            print(f'Fecha :{self.fecha}')
            print(f'Titular de la cuenta: {self.titular}')
            print(f'Operación Realizada: {self.tipo}')
            print(f'Saldo : {self.saldo}')
            print(f'Saldo : {self.movimientos}')

    def mostrar_saldo(self):
        # Completar lo siguiente: 
        # 1. mostrar mensaje con nombre de titular y su saldo.
        fecha = '28-03-2025'
        self.fecha = fecha
        tipo = 'Consulta de Saldo'
        self.tipo = tipo

        print('\nConsulta de Saldo')
        print(f'Fecha :{self.fecha}')
        print(f'Titular de la cuenta: {self.titular}')
        print(f'Operación Realizada: {self.tipo}')
        print(f'Saldo : {self.saldo}')

    def mostrar_movimientos(self):
        print(f"\n--- Historial de {self.titular} ---")
        # Completar lo siguiente: 
        # 1. iterar la lista de movimientos y mostar la fecha, tipo el monto y el saldo.
        
        for operacion in self.movimientos:

            fecha = operacion[0]
            tipo = operacion[1]
            monto = operacion[2]
            saldo = operacion[3]
            print(f'{fecha}\t{tipo}\t{monto}\t{saldo}')

