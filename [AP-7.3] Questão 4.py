from biblioteca import *

def identidade (matriz):
    l, c = dimMatriz (matriz)
    for i in range (l):
        for j in range (c):
            if i == j:
                if matriz[i][j] != 1:
                    return False
            else:
                if matriz[i][j] != 0:
                    return False
    return True

matriz = inputMatriz ('Digite os elementos da matriz: ', int)
if identidade(matriz):
    print ('A matriz é identidade.')
else:
    print ('A matriz não é identidade.')