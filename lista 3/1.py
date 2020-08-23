speed=float(input('insira a velocidade\n'))
if(speed>80):
    speed=speed-80
    print('Você foi multado - valor da multa: {0:.3f}'.format(5*speed))
else:
    print('Dentro da Velocidade permitida')
