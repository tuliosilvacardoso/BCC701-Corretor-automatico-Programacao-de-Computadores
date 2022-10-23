juiz = input("Informe o nome do juiz: ")
nPartidas = int(input("Quantidade de partidas: "))
imp = 0
fal = 0 
cart = 0
temp = 0
print()
for n in range(nPartidas):
    print(f"Partida {n+1}:")
    imp += int(input(". Impedimentos.......: "))
    fal += int(input(". Faltas.............: "))
    cart += int(input(". Cartões............: "))
    temp += float(input(". Tempo de acréscimo.: "))
    print()
print(f"Estatísticas do juiz {juiz}:")
print(f". Impedimentos.......: {imp/nPartidas:.2f}.")
print(f". Faltas.............: {fal/nPartidas:.2f}.")
print(f". Cartões............: {cart/nPartidas:.2f}.")
print(f". Tempo de acréscimo.: {temp/nPartidas:.2f}.")