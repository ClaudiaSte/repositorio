vel = float(input('Qual é a velocidade atual do carro? '))
if  vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('O valor da multa é de R$ {:.2f}'.format((vel - 80) * 7))
else:
    print('Tenha um bom dia! Dirija com segurança!')