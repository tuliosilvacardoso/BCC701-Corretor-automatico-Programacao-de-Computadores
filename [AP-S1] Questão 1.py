valor = float(input("Defina o valor total da compra: "))
if valor <= 0:
    d = 0
    print ("Erro: Valor total inválido.")
else:
    if valor <= 250:
        d = 0.97
    elif valor > 250 and valor <= 550:
        d = 0.94
    elif valor > 550 and valor <= 750:
        d = 0.92
    else:
        d = 0.9
    valorDesconto = valor * d
    print(f"Desconto de {100-(0.97*100):.0f}%")
    print(f"Valor com desconto: R$ {valorDesconto:.2f}")