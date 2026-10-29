tab = int(input('Digite um número para ver sua tabúada: '))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(tab, i, tab*i))