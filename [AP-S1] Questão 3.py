def avaliaApresentacao(Njuizes):
    A = 1
    pontosTotais = 0
    grau = float(input(". Grau de dificuldade: "))
    while A <= Njuizes:
        Nota = float(input(f". Nota do juíz {A}: "))
        A += 1
        pontosTotais += Nota
    print(f".Pontuação da apresentação: {pontosTotais*grau:.2f} ")
Napresentacoes = int(input("Defina a quantidade de apresentações: "))
Njuizes = int(input("Defina a quantidade de juízes: "))
B = 1
while B <= Napresentacoes:
    print(f". Apresentação {B}:")
    x = avaliaApresentacao(Njuizes)
    B += 1 