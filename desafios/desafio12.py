alt = float(input('Digite a altura da parede em metros: '))
lar = float(input('Digite a largura da parede em metros: '))
area = alt * lar
tinta = area / 2
print(f'Sua parede tem a dimensão de {alt}x{lar} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')