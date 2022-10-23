import math


def calculaF(x, y):
    if -math.inf < x <= 30:
        func = (x ** 2) + (2 * y) - 3
    elif 30 < x <= 60:
        func = math.sin(0.0175 * x) * math.cos(0.0175 * y)
    elif 60 < x <= 90:
        func = 1 / (x ** (-2)) + y
    else:
        func = math.pi
    return round(func, 2)


# Entradas do usuário
Ini = int(input("Valor inicial: "))
while 50 < Ini or Ini < -150:
    Ini = int(input("Valor inicial: "))
Fim = int(input("Valor final: "))
while Fim <= Ini:
    Fim = int(input("Valor final: "))
Passo = int(input("Passo: "))
while Passo <= 0:
    Passo = int(input("Passo: "))

# Primeira Linha / Enunciado
print(f"x \ y |", end="")
count = 0
for i in range(Ini, Fim + 1, Passo):
    print(f"{i:10d}", end="")
    count += 1
print("\n-------", end="")
print("----------" * count)

# Calculo e disposição da função na tabela
for x in range(Ini, Fim + 1, Passo):
    print(f"{x:5d} |", end="")
    for y in range(Ini, Fim + 1, Passo):
        a = f"{calculaF(x, y):.2f}"
        print(f"{a:>10}", end="")
    print()