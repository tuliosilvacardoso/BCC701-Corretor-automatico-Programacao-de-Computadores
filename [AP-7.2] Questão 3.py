import biblioteca
def contabilizarDemandas(r):
    a = 0
    b = 0
    c = 0
    x = 0
    for i in range(len(r)):
        if r[i] >= 85:
            a+= 1
        elif r[i] >= 65 and r[i] < 85:
            b+= 1
        elif r[i] >= 45 and r[i] < 65:
            c += 1
        elif r[i] >= 18 and r[i] < 45:
            x += 1
    t = biblioteca.criarVetor(0,0)
    t.append(a)
    t.append(b)
    t.append(c)
    t.append(x)
    return t
def avaliaAtendimento(t,dis):
    conf = 0
    for i in range(len(t)):
        if t[i] <= dis[i]:
            conf += 1
    if conf == len(t):
        return True
    else:
        return False
            
        
c = biblioteca.inputVetor('Defina as idades dos habitantes: ', int)
t = contabilizarDemandas(c)
print('Demandas a serem atendidas por faixa etária:')
for i in range(len(t)):
    if i == 0:
        print(f'. >= 85.........: {t[i]}')
    elif i == 1:
        print(f'. < 85 e >= 65.: {t[i]}')
    elif i == 2:
        print(f'. < 65 e >= 45.: {t[i]}')
    elif i == 3:
        print(f'. >= 18.........: {t[i]}')
        
dis = biblioteca.inputVetor('Defina as disponibilidades de vacinas: ', int)
av = avaliaAtendimento(t,dis)

if av == True:
    print('A quantidade de vacinas é suficiente.')
if av == False:
    print('Infelizmente, precisaremos de mais vacinas.')
