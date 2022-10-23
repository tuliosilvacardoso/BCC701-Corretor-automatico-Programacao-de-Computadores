from biblioteca import *

print('Ministério do Meio Ambiente')

v = inputVetor('Metas dos estados: ', int)
m = inputMatriz('Plantio de árvores: ', int)
for i in range(len(v)):
    soma = 0
    for j in range(len(m)):
        soma += m[j][i]
    if v[i] > soma:
        print(f'Estado {i+1}, meta = {v[i]}, plantio = {soma}')