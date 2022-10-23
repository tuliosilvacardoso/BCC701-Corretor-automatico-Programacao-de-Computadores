import math
q = int(input("Digite a quantidade de lados: "))
if q < 3:
    print(f'Não é um polígono')
elif q > 6:
    print(f'Polígono não identificado')
else:
    l = float(input("Digite a medida do lado: "))
    if q == 3:
        a = ((l**2)*math.sqrt(3) / 4)
        p = 'triângulo'
    elif q == 4:
        a = l**2
        p = 'quadrado'
    elif q == 5:
        a = (5 * (l**2) / (4 * (math.tan(0.6283))))
        p = 'pentágono'
    else:
        a = 3 * (l**2) * (math.sqrt(3)) / 2
        p = 'hexágono'
    print(f'O polígono é um {p} com área: {a:.2f}')
