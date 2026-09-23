import random
n = int(input('Digite um número de 1 a 5: '))
num = [1, 2, 3, 4, 5]
random.choice(num)
print('O número sorteado foi {}'.format(random.choice(num)))
if n == random.choice(num):
    print('Você acertou!')
else:
    print('Você errou!')