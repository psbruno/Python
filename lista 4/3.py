matriz=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=int(input('insira um numero\n'))
for i in range(0,3):
    for j in range(0,3):
        print('[',matriz[i][j],']', end=' ')
    print()
