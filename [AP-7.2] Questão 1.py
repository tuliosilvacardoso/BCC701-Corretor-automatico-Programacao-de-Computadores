import biblioteca
def calculaLucros(c,q,lc,lq):
    soma = []
    for i in range(len(c)):
        soma.append(round((c[i]*lc) + (q[i]*lq),2))
    return soma
    
c = biblioteca.inputVetor('Vendas de coxinhas: ', int)
q = biblioteca.inputVetor('Vendas de quibes: ', int)
if len(c) == len(q):
    lc = float(input('Lucro por unidade de coxinha: R$ '))
    lq = float(input('Lucro por unidade de quibe: R$ '))
    soma = calculaLucros(c,q,lc,lq)
    print(f'Lucros: {soma}')
    print(f'Maior lucro: R$ {max(soma):.2f}')
    print(f'Menor lucro: R$ {min(soma):.2f}')
else:  
    print('Dados de vendas inválidos')