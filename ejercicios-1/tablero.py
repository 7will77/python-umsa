'''
# # # # # # # #         00 01 02 03
 # # # # # # # #        10 11 12 13
# # # # # # # #         20 21 22 23
'''

dimension = input('Dimension del tablero: ')
dimension = int(dimension)

for i in range(0,dimension):
    for j in range(0,dimension):
        if (i+j) % 2 == 0:
            print(f'# ', end='')
        else:
            print(f'  ', end='')
    print ('')


