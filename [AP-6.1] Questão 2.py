def Fatorial(n):
    while n<=0:
            n=int(input('Número inválido, defina outro: '))
    ni=n
    if n>0:
        while n-1>1:
            ni=ni*(n-1)
            n=n-1
    return ni
n = int(input('Informe o número que deseja calcular o Fatorial: '))
ni = Fatorial(n)
print(f'O Fatorial de {n} é: {ni}')