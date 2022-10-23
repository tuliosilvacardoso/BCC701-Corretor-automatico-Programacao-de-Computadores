import biblioteca
def comparaVetores(c,q):
    r = []
    for i in range(len(c)):
        if c[i] > q[i]:
            r.append('R')
        if c[i] < q[i]:
            r.append('A')
        if c[i] == q[i]:
            r.append('E')
    return r
def classificaEstado(r):
    R = 0
    A = 0
    E = 0
    for i in range(len(r)):
        if r[i] == 'R':
            R+= 1
        elif r[i] == 'A':
            A+= 1
        elif r[i] == 'E':
            E += 1
    if R > A:
        return 'Onda Verde'
    elif R < A:
        return 'Onda Vermelha'
    elif R == A:
        return 'Onda Amarela'
    
c = biblioteca.inputVetor('Número de mortes na semana anterior: ', int)
q = biblioteca.inputVetor('Número de mortes na semana atual: ', int)
if len(c) == len(q):
    r = comparaVetores(c,q)
    e = classificaEstado(r)
    print(f'Classificações das macro-regiões:\n{r}')
    print(f'Classificação do estado: {e}')
    
else:  
    print(f'Número de elementos incompatível ({len(c)} != {len(q)})')
