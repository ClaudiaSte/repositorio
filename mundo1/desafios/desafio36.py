print('-=-' * 20)
print('Analisando segmentos de um triângulo')
print('-=-' * 20)
ret1 = float(input('Digite o primeira segmento: '))
ret2 = float(input('Digite a segunda segmento: '))
ret3 = float(input('Digite a terceira segmento: '))
if ret1 < ret2 + ret3 and ret2 < ret1 + ret3 and ret3 < ret1 + ret2:
    print('Os segmentos PODEM formar um triângulo')
else:
    print('Os segmentos NÃO PODEM formar um triângulo')