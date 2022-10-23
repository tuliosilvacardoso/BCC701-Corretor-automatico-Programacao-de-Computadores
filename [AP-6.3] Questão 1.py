def imprimeRetangulo(altura, largura):
    for i in range(altura):
        for j in range(largura):
            print('*', end='')
        print()


imprimir = input("Deseja imprimir um retângulo? (s/n) ")
while imprimir == "s":
    altura = int(input("\nAltura do retângulo: "))
    largura = int(input("Largura do retângulo: "))
    while altura >= largura or altura <= 0 or largura <= 0:
        print("Entrada inválida.")
        altura = int(input("\nAltura do retângulo: "))
        largura = int(input("Largura do retângulo: "))
    print("")
    imprimeRetangulo(altura, largura)
    imprimir = input("\nDeseja imprimir outro retângulo? (s/n) ")