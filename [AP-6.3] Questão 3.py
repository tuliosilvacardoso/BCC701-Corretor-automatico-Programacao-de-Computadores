def verifier(j):
    if j == 'sim':
        return True
    else:
        return False


print('Caixa aberto!')
quant = 0
total = 0
j = 0
while not verifier(j):
    quant_pedidos = int(input('\nQuantidade de itens do pedido: '))
    valor = 0
    for i in range(1, quant_pedidos+1):
        price = float(input(f'. Preço do item {i}: '))
        valor += price
    j = input('. Cobrar delivery? ')
    if verifier(j):
        valor += 15
    print(f'. Valor do pedido: R$ {valor:.2f}.')
    quant += 1
    total += valor
    j = input('Fechar o caixa? ')
print(f'\nCaixa fechado!\nNúmero de pedidos: {quant}.\nValor total vendido: R$ {total:.2f}.')