import math
tipo = input("Tipo de ladrilho (1 ou 2): ")
A = float(input("Área da sala: "))
if tipo == 1:
    qtde = A/60
else:
    qtde = A/80
print(f"Quantidade de ladrilhos: {math.ceil(qtde)}")
