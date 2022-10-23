def calculaJ(capital, meses):
    if capital <= 10000:
        taxa = 0.1
    else:
        taxa = 0.07
    juros = capital * taxa * meses #Juros
    taxa = round(taxa*100)  #taxa em %
    return juros, taxa


Total = float(input('Capital Total para empréstimo: '))
capital = float(input('Capital emprestado: '))
if capital > Total:
    print(f'Empréstimo negado, capital total é de R$ {Total:.2f}')
else:
    while capital <= Total:
        meses = float(input('Quantidade de meses para quitação: '))
        juros, taxa = calculaJ(capital, meses)
        print(f'Taxa de juros aplicada: {taxa}%.\nJuros devido: {juros:.2f}.\nValor total: {capital + juros:.2f}.')
        Total = Total - capital
        capital = float(input('Capital emprestado: '))
    print(f'Empréstimo negado, capital total é de R$ {Total:.2f}.')