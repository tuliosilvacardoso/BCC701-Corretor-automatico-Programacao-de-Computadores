import math

def minimo(a, b):
    if a < b:
        return a
    else:
        return b

def maximo(a, b):
    if a > b:
        return a
    else:
        return b

def calcDano(a, b, d):
    return minimo(999, math.trunc(a * (1 + b) * (1 - d / (100 + d))))

def vidaAposGolpe(v, a, b, d):
    return maximo(0, v - calcDano(a, b, d))

f1 = int(input('Força de ataque do personagem 1: '))
f2 = int(input('Força de ataque do personagem 2: '))
f3 = int(input('Força de ataque do personagem 3: '))
f4 = int(input('Força de ataque do personagem 4: '))
d = int(input("Força de defesa do inimigo: "))
v = int(input("Vida inicial do inimigo: "))

v = vidaAposGolpe(v, f1, 0.15, d)
v = vidaAposGolpe(v, f2, 0, d)
v = vidaAposGolpe(v, f3, 0, d)
v = vidaAposGolpe(v, f4, 0.15, d)

print(f'A vida do inimigo será: {v:.0f}')