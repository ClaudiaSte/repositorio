from math import hypot
cat = float(input("Digite o valor do cateto oposto: "))
cat2 = float(input("Digite o valor do cateto adjacente: "))
hip = hypot(cat, cat2)
print("O valor da hipotenusa é: {:.2f}".format(hip))