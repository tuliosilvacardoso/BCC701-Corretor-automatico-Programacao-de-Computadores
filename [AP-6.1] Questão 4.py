def perfeito(n):
    soma = 0
    for i in range(1, n):
        if n% i == 0:
            soma += i
    return soma


n = int(input('Digite um número: '))
while n > 0:
    soma = perfeito(n)
    if soma == n:
        print(f'{n} == {soma}: número é perfeito')
    else:
        print(f'{n} <> {soma}: número não é perfeito')
    n = int(input('Digite um número: '))
    