from biblioteca import *

print('Loja da tia Maria')
m = inputMatriz('Matriz de estoque: ', int)
nAt = int(input('Número de atualizações: '))
for i in range(nAt):
    l = int(input('Índice da loja: '))
    p = int(input('Índice do produto: '))
    novo = int(input('Novo estoque: '))
    m[l][p] = novo
    for i in range (len(m)):
        print(m[i])