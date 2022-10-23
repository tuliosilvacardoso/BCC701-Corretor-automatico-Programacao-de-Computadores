from biblioteca import *

matriz = inputMatriz ('Digite os elementos da matriz: ', int)

linhas, colunas = dimMatriz (matriz)

x = int (input ('Digite a coluna que será alterada: '))
while x < 0 or x >= colunas:
    x = int (input ('\nDigite uma coluna válida: '))

for i in range (linhas):
    matriz[i][x] *= 2


print ('\nMatriz alterada:')
for i in range (linhas):
    for j in range (colunas):
        if j != colunas - 1:
            print (f'{matriz[i][j]}', end=', ')
        else:
            print (f'{matriz[i][j]}', end='')
    if i != linhas - 1:
        print ('; ', end='')
    else:
        print ()