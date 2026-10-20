nome = str(input('Qual é seu nome? '))
if nome == 'Cláudia':
  print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Ana':
  print('Seu nome é bem popular no Brasil')
elif nome in ('Carol Morgana Adelinne Aurora'):
  print('Que belo nome femenino!')
else:
  print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))