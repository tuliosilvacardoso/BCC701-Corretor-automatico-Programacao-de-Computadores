p = float(input("Digite seu peso (em kg): "))
h = float(input("Digite sua altura (em metros): "))
s = input("Seu sexo é masculino (M) ou feminino (F)? ")
IMC = (p / (h**2))
if s == 'M':
    if IMC > 25:
        pn = 25 * (h**2)
        print(f'Você deve perder {p-pn:.2f}kg para ter IMC = 25')
    else:
        print(f'Você não precisa perder peso para ter IMC <= 25')
elif s == 'F':
    if IMC > 24:
        pn = 24 * (h**2)
        print(f'Você deve perder {p-pn:.2f}kg para ter IMC = 24')
    else:
        print(f'Você não precisa perder peso para ter IMC <= 24')
else:
    print(f'A entrada contém dados não reconhecidos')
    
        
        
        
        
        
    