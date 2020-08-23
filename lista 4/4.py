Unifesp = dict()
aluno = list()

i=int(input('insira o RA\n'))
while(i!=-1):
    Unifesp['RA']=i
    Unifesp['Nota']=float(input('insira a nota\n'))
    if Unifesp['Nota']>=6:
        Unifesp['Situacao']='Aprovado'
    elif Unifesp['Nota']>=3 and Unifesp['Nota'] <6:
        Unifesp['Situacao']= 'Exame'
    else:
        Unifesp['Situacao']='Reprovado'
    aluno.append(Unifesp.copy())
    i = int(input('insira o RA\n'))
for j in aluno:
    for k in j.values():
        print(k, end = ' ')
        print()
