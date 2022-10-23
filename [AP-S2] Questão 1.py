from biblioteca import *
import math
print("Manipulações de valores de Vetor")
vetor = inputVetor ("Vetor X: ", float)
print("Propriedades do vetor X: ")
def calculosVetor(vetor):
    soma = 0
    A = len(vetor)
    maior = -math.inf
    menor = math.inf
    for i in range (len(vetor)):
        if menor > vetor[i]:
            menor = vetor[i]
        if maior < vetor[i]:
            maior = vetor[i]
        soma += vetor[i]
    media = round(soma/len(vetor), 2)
    return A, menor, maior, media 
x, y, w, z = calculosVetor(vetor)
print(f". Possui {x} elementos")
print(f". {y:.2f} é o menor valor")
print(f". {w:.2f} é o maior valor")
print(f". A média dos valores é {z}")
