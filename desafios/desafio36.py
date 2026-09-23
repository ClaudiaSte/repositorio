ret1 = int(input('Digite a primeira reta: '))
ret2 = int(input('Digite a segunda reta: '))
ret3 = int(input('Digite a terceira reta: '))
if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')