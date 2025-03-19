matriz = [
    [10, 12, 14, 16, 18],
    [20, 22, 24, 26, 28]
]
'''
for i in range(0,2):
    for j in range(0,5):
        print(f'indice: ({i},{j}) = {matriz[i][j]}')
'''
print('Como Tabla...')
for i in range(0,2):
    for j in range(0,5):
        print(f'{matriz[i][j]} ', end='')
    print ('')
