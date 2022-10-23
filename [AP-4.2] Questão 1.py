import math
c = float(input("Capital emprestado: "))
m = int(input("Quantidade de meses para quitação: "))
if c <= 10000:
    t = 0.1
else:
    t = 0.07
J = c * t * m
print(f'Taxa de juros aplicada: {t*100:.0f}%')
print(f'Juros devido: {J:.2f}')
print(f'Valor total: {c+J:.2f}')