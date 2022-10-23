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

def acimaMedia(Notas, Corte):
    Indices = []
    for x in range(len(Notas)):
        if Notas[x] > Corte:
            Indices.append(x)
    return Indices       
            
    


Notas = inputVetor('Notas: ', float)
Maior_nota, Menor_nota, Nota_media = estatNotas(Notas)

print(f'Maior nota: {Maior_nota}')
print(f'Menor nota: {Menor_nota}')
print(f'Nota média: {Nota_media}')

Indices = acimaMedia(Notas, Nota_media)
print(f'Notas acima da média: ')
for x in range(len(Indices)):
    print(f' - [{Indices[x]}] = {Notas[Indices[x]]}')
    
    

