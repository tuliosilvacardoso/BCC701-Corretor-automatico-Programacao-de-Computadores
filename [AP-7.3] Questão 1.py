from biblioteca import *

notas = inputMatriz ('Matriz de notas: ', float)

linhas, colunas = dimMatriz (notas)

maiorNota = -1.0
menorNota = 11.0

for i in range (linhas):
    for j in range (colunas):
        if notas[i][j] > maiorNota:
            maiorNota = notas[i][j]
        if notas[i][j] < menorNota:
            menorNota = notas[i][j]


menorA = []
maiorA = []

for i in range (linhas):
    for j in range (colunas):
        if notas[i][j] == maiorNota:
            maiorA.append (i)
        if notas[i][j] == menorNota:
            menorA.append (i)

print (f'\nMenor nota: {menorNota}')
print ('Alunos com a menor nota:')
for i in range (len(menorA)):
    print (f'. {menorA[i]}')

print (f'\nMaior nota: {maiorNota}')
print ('Alunos com a maior nota:')
for i in range (len(maiorA)):
    print (f'. {maiorA[i]}')