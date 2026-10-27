tab = int(input('Digite um número para ver sua tabúada: '))
print(f'A tabuada de é: '.format(tab))
for i in range(1, 11):
    print(f'{tab} x {i} = {tab * i}')