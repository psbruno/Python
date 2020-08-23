primo=list()
nprimo=list()
for i in range(0,10):
    n = int(input('insira um numero\n'))
    a = 0
    for j in range(2, n):
        if (n % j == 0):
            a = 1
    if (a == 0):
        primo.append(n)
    else:
        nprimo.append(n)
print('primos:',primo,'\nNao primos:', nprimo)
