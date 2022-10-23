def realizaCalculos(n, R):
    pi = 0
    for i in range (0,n):   
        pi += ((-1)**i)*(4/(2*i+1))
    V = (4/3)*pi*R**3
    return round(pi, 5),round(V, 5)
n = int(input("Número de termos: "))
R = int(input("Raio da esfera: "))
x, y = realizaCalculos(n, R)
print(f"pi = {x}.")
print(f"Volume da esfera = {y}.")
