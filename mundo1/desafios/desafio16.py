km = float(input("Quantos kilometros foram percorridos?"))
dias = int(input("Por quantos dias o carro foi alugado?"))
total = km * 0.15 + dias * 60
print('O total a pagar é de R${:.2f}.'.format(total))
