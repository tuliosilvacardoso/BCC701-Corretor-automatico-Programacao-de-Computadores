c = float(input("Comprimento de corte dos tubos: "))
erro = float(input("Margem de erro aceitável: "))
qtde = int(input("Quantidade de tubos demandada: "))
x = qtde+1
while x>-1:
    C = float(input("Comprimento do tubo cortado: "))
    if C > c+erro or C < c-erro:
        print("Acima da margem de erro, tubo rejeitado")
    else:
        x =- 1
def avaliaTubo(C,c,erro):  
    if c - erro > C or c + erro < C:
        return False
    else:
        return True
print(f"Total de tubos cortados: {qtde-x}")
print(f"Total de tubos rejeitados: {x} ")
 
    
    