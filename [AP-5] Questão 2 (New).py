def converteMedidas(M):
    FT = 0.3048*M
    YD = 0.9144*M
    return round(FT, 3), round(YD, 3)
print ("Percurso 1: ")
M = float(input("  - Tamanho em metros: "))
FT,YD = converteMedidas(M)
print(f"  - Tamanho em pés...: {FT:.2f}")
print(f"  - Tamanho em jardas: {YD:.2f}")
print ("Percurso 2: ")
M = float(input("  - Tamanho em metros: "))
FT,YD = converteMedidas(M)
print(f"  - Tamanho em pés...: {FT:.2f}")
print(f"  - Tamanho em jardas: {YD:.2f}")
print ("Percurso 3: ")
M = float(input("  - Tamanho em metros: "))
FT,YD = converteMedidas(M)
print(f"  - Tamanho em pés...: {FT:.2f}")
print(f"  - Tamanho em jardas: {YD:.2f}")