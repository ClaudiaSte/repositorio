sal = float(input("Digite o salário do funcionário: "))
if sal > 1250:
    aumento = sal * 0.10
    print("O aumento do salário é R$ {:.2f}".format(aumento))
else:
    aumento = sal * 0.15
    print("O aumento do salário é R$ {:.2f}".format(aumento))