distancia = float(input('Qual a distância da viagem em km? ')) 
print('Você está prestes a começar uma viagem de {} km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da passagem é R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('O preço da passagem é R${:.2f}'.format(preco))