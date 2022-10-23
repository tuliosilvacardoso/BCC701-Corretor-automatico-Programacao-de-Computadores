nome = input("Informe o nome do produto: ") 
while nome != "fim":
    V = float(input("Valor do pedido: "))
    if nome == "Pão de queijo":
        if V <= 50:
            d = 10
        elif V > 50 or V <= 100:
            d = 12
        else:
            d = 15
    elif nome == "Pastel de angu":
        if V <= 50:
            d = 9
        elif V > 50 or V <= 100:
            d = 10
        else:
            d = 11
    print(f"Percentual de desconto: {d:.2f}%")
    print(f"Valor com desconto: R$ {V-(V*0.01*d):.2f}")
    nome = input("Informe o nome do produto: ")
    
