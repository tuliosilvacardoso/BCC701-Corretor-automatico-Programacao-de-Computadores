def impostoRenda(B):
    if B < 1500:
        p = 0
    elif B < 2500:
        p = 5
    elif B < 4500:
        p = 10
    else:
        p = 20
    IR = p/100 * B
    return round(IR, 2)
B = float(input("Digite o salário bruto: "))
IR = impostoRenda(B)
print(f"(-)IR: R$ {IR:.2f}")
print(f"(-)INSS: R$ {B*0.1:.2f}")
print(f"FGTS: R$ {B*0.11:.2f}")
print(f"Total de descontos: R$ {B*0.1+IR:.2f}")
print(f"Salário Líquido: R$ {B-(B*0.1)-IR:.2f}")