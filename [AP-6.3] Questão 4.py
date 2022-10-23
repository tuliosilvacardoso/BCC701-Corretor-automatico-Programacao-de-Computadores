meta_nacional = float(input('Meta Nacional: R$ '))
total_estadual = 0
quant = 1
while total_estadual < meta_nacional:
    nome_estado = input(f'. Nome do estado {quant}: ')
    meta_estadual = float(input('. Meta estadual: R$ '))
    quant += 1
    total_cidades = 0
    quant_cidade = 0
    while total_cidades < meta_estadual:
        vendas_cidade = float(input(f'.. Vendas na cidade {quant_cidade+1}: R$ '))
        total_cidades += vendas_cidade
    print(f'.. Meta no estado {nome_estado} cumprida!\n.. Total do estado: R$ {total_cidades:.2f}.')
    total_estadual += total_cidades
print(f'Meta nacional cumprida!\nTotal nacional: R$ {total_estadual:.2f}.')