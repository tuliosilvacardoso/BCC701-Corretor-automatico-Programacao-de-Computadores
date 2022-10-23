from biblioteca import *

matriz = inputMatriz ('Digite os elementos da matriz: ', int)

linhas, colunas = dimMatriz (matriz)

if (linhas != colunas):
    print ('\nA matriz não é quadrada.')
else:
    print ('\nElementos da diagonal principal:')
    for i in range (linhas):
        if i != linhas - 1:
            print (f'{matriz[i][i]}', end=', ')
        else:
            print (f'{matriz[i][i]}')
