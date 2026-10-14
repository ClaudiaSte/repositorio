nome = str(input('Digite uma frase ou nome: ').lower().strip())
print('A letra A aparece {} vezes na frase.' .format(nome.count('a')))

print('A primeira letra A apareceu na posição {}'.format(nome.find('a') + 1))

print('A última letra A apareceu na posição {}'.format(nome.rfind('a') + 1))