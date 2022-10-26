nA = int(input('Quantidade de alunos: '))
nD = int(input('Quantidade de disciplinas: '))
alunos = [ ]
for a in range(nA):
    linha = [ ]
    print(f'\nDados do aluno {a+1}:')
    for d in range(nD):
        aluno = { }
        print(f' - Dados da disciplina {d+1}:')
        aluno["nota"] = float(input(' - Nota: '))
        aluno["freq"] = int(input(' - Frequência: '))
        linha.append(aluno)
    alunos.append(linha)
print('\nDados das disciplinas com maiores notas:')
for a in range(nA):
    maior = 0
    for d in range(nD):
        if alunos[a][d]["nota"] > alunos[a][maior]["nota"]:
            maior = d
    print(f' - Aluno {a+1}: nota = {alunos[a][maior]["nota"]:.1f}; frequência = {alunos[a][maior]["freq"]}')
