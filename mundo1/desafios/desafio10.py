tab = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuada de {tab} é:')
for i in range(1, 11):
    print(f'{tab} x {i} = {tab * i}')