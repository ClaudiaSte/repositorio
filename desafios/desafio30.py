vel = float(input('Qual é a velocidade do carro? '))
if  vel > 80:
    print('Você foi multado!')
    print('O valor da multa é de R$ {:.2f}'.format((vel - 80) * 7))