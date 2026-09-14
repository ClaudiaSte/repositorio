n = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome com todas as letras maiúsculas é{}:'.format(n.upper()))
print('Seu nome com todas as letras minúsculas é{}:'.format(n.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(n.find(' ')))