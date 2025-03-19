#Programa para realizar el conteo de las 5 vocales en una frase que se introduce

frase = input('Ingresa una palabra:')
cantidad_letras = len(frase)

#Definimos variables que nos permitiran contar la existencia de Vocales
cont_a=0
cont_e=0
cont_i=0
cont_o=0
cont_u=0

#Barremos la frase verificando la ocurrencia de alguna vocal
for i in range(cantidad_letras):
    if frase[i] == 'a':
        cont_a += 1
    elif frase[i] == 'e':
        cont_e +=1
    elif frase[i] == 'i':
        cont_i +=1   
    elif frase[i] == 'o':
        cont_o +=1
    elif frase[i] == 'u':
        cont_u +=1

#Presentacion de la ocurrencia de vocales en la frase
print(f'La vocal \'a\' aparece {cont_a} veces')
print(f'La vocal \'e\' aparece {cont_e} veces')
print(f'La vocal \'i\' aparece {cont_i} veces')
print(f'La vocal \'o\' aparece {cont_o} veces')
print(f'La vocal \'u\' aparece {cont_u} veces')
