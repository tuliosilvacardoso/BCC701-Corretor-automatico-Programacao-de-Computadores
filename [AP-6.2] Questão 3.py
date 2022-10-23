votoVal = 0
votoInVal = 0
voto1 = 0
voto2 = 0
nome1 = input("Nome do candidato 1: ")
n1 = float(input("Número do candidato 1: "))
nome2 = input("Nome do candidato 2: ")
n2 = float(input("Número do candidato 2: "))
qtde = int(input("Quantidade de eleitores: "))
while qtde < 3:
    print("A quantidade de eleitores é inferior a 3")
    qtde = int(input("Quantidade de eleitores: "))

print()
print("## Votação Iniciada")
for n in range (qtde):
    numero = float(input("Número do candidato que deseja votar: "))
    if numero == n1:
        votoVal += 1
        voto1 +=1
    elif numero == n2:
        votoVal +=1
        voto2 += 1
    else:
        votoInVal += 1
print("## Votação Encerrada")
print()
print(f"Votos válidos: {(votoVal/qtde)*100:.2f}% ({votoVal} votos)")
print(f"Votos inválidos: {(votoInVal/qtde)*100:.2f}% ({votoInVal} votos)")
if votoVal != 0:
    print(f"Votos para {nome1}: {(voto1/votoVal)*100:.2f}% ({voto1} votos)")
    print(f"Votos para {nome2}: {(voto2/votoVal)*100:.2f}% ({voto2} votos)")
else:
    print(f"Votos para {nome1}: 0.00% ({voto1} votos)")
    print(f"Votos para {nome2}: 0.00% ({voto2} votos)")

