nome = input("Entre com o nome: ")
idade = float(input("Entre com a idade: "))
sexo = input("Entre com o sexo (m ou f): ")
if sexo == "m":
    if idade < 18:
        print(f"Faltam {18-idade:.1f} anos para {nome} atingir a maioridade")
    else:
        print(f"{nome} tem maioridade civil")
if sexo == "f":
    if idade < 21:
        print(f"Faltam {21-idade:.1f} anos para {nome} atingir a maioridade")
    else:
        print(f"{nome} tem maioridade civil")
        
        