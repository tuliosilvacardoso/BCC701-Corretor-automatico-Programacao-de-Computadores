h = float(input("Digite a altura: "))
sexo = input("Qual é o sexo (m ou f): ")
if sexo == "m":
    P = (72.7*h)-58
    print(f"O peso ideal é: {P:.2f}")
else:
    P = (62.1*h)-44.7
    print(f"O peso ideal é: {P:.2f}")
    