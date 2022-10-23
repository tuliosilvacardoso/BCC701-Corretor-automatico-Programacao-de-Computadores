from biblioteca import *

def estatNotas(Notas):
    Tamanho = len(Notas)
    Maior = 0 
    Menor = 11
    Media = 0
    for i in range(Tamanho):
        if Notas[i] > Maior:
            Maior = Notas[i]
        if Notas[i] < Menor:
            Menor = Notas[i]
        Media +=Notas[i]
    Media = Media/Tamanho
    return(round (Maior, 1), round (Menor, 1), round (Media, 1))

         

Notas = inputVetor('Notas: ', float)
Maior_nota, Menor_nota, Nota_media = estatNotas(Notas)

print(f'Maior nota: {Maior_nota}')
print(f'Menor nota: {Menor_nota}')
print(f'Nota média: {Nota_media}')

    

