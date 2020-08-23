v0=int(input('insira o primeiro termo\n'))
r=int(input('insira a razão\n'))
for i in range (0, 10):
    print('valor {} - {}\n '.format(i+1, v0))
    v0+=r;
