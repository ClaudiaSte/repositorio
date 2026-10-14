sal = float(input("Digite o salário do funcionário: "))
if sal <= 1250:
    aumento = sal + (sal * 15 / 100)
else:
    aumento = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, aumento))