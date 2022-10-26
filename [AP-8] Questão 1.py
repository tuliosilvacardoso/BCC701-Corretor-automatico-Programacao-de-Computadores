from biblioteca import *
import math
def calculaComprimento(r):
    d1 = r["B"]["X"] - r["A"]["X"]
    d2 = r["B"]["Y"] - r["A"]["Y"]
    c = round(math.sqrt(d1 ** 2 + d2 ** 2), 2)
    return c

q = int(input('Informe a quantidade de retas: '))
p = 1
media = 0
m = []
v = []
while p <= q:
    print('')
    print(f'Reta {p}:')
    A = {}
    A["X"] = float(input('- Coordenada X de A: '))
    A["Y"] = float(input('- Coordenada Y de A: '))
    B = {}
    B["X"] = float(input('- Coordenada X de B: '))
    B["Y"] = float(input('- Coordenada Y de B: '))
    r = {"A":A, "B": B}
    y = calculaComprimento(r)
    m.append(r)
    v.append(y)
    p+=1
print('')
print('Medidas das retas:')
for i in range(len(m)):
    print(f'- Reta {i+1}: {v[i]}')