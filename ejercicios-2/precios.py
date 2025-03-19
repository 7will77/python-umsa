# Creamos la lista con los precios
lista = [50, 75, 46, 22, 80, 65, 3, 15]
minimo = lista[0]
maximo = lista[0]
for precio in lista:
    if precio < minimo:
        minimo = precio
    if precio > maximo:
        maximo = precio
print(f'El mínimo es: {minimo} \nEl máximo es: {maximo}')
