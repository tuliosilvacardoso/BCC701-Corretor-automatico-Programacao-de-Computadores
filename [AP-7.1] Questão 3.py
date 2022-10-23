import math
def inputVetor(mensagem, conversao):
    valores = input(mensagem)
    resultado = [ ]
    if valores == '':
        return resultado
    valores = valores.split(',')
    for i in range(len(valores)):
        valor = conversao(valores[i].strip())
        resultado.append(valor)
    return resultado
def estatNotas(x):
    m=0
    for y in range(len(x)):
        m+= x[y]
    m=m/len(x)
    ma=x[0]
    m=round(m,1)
    for y in range(len(x)):
        if ma< x[y]:
            ma=x[y]
    mn=x[0]
    for y in range(len(x)):
        if mn > x[y]:
            mn=x[y]

    return ma,mn,m
def acimaMedia(x8,y8):
    x=[]
    for y in range(len(x8)):
        if x8[y]>y8:
            x.append(y)
            
    return x
def exameEspecial(vtn):
    q=[]
    for p in range(len(vtn)):
        if vtn[p]>=3 and vtn[p]<6:
            q.append(p)
    return q
x1=inputVetor('Notas: ',float)
n1=inputVetor('Nomes: ',str)
r,l,j=estatNotas(x1)
x9=acimaMedia(x1,j)
x7=exameEspecial(x1)
print(f'Maior nota: {r:.1f}') 
print(f'Menor nota: {l:.1f}')
print(f'Nota média: {j:.1f}')
print('Notas acima da média:')
for r in range(len(x9)):
    y=0
    g=0
    while y<len(x1):
        if x1[x9[r]]==x1[y]:
            print(f' - [{x9[r]}] = {x1[y]:.1f} ({n1[x9[r]]})')
            y=len(x1)
        y+=1
print('Notas em Exame Especial: ')
for h in range(len(x7)):
    print(f' - [{x7[h]}] = {x1[x7[h]]:.1f} ({n1[x7[h]]})')

