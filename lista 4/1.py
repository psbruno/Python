Maior=0
Menor=100000000000
Media=0
i=1
j=0
Sala=list()
Aluno=list()
while i != 0:
    Aluno.append(str(input('insira o nome do aluno\n')))
    Aluno.append(int(input('insira a nota do aluno\n')))
    Sala.append(Aluno[:])
    Aluno.clear()
    j=j+1
    i = int(input('Para encerrar, digite 0, inserir um novo aluno 1\n'))
for p in Sala:
    Media=p[1]+Media
    if p[1]>Maior:
        Maior=p[1]
    if p[1]<Menor:
        Menor=p[1]
print('Alunos e Notas:\n',Sala)
print(' Numero de alunos:{}\n Maior Nota:{}\n Menor Nota:{}\n Media:{}\n'.format(j, Maior, Menor, Media/j))
