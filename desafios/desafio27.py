nome = input('Digite uma frase ou nome: ').strip()
print('A letra A aparece {} vezes na frase.' .format(nome.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(nome.lower().find('a') + 1))
print('A última letra A apareceu na posição {}'.format(nome.lower().rfind('a') + 1))