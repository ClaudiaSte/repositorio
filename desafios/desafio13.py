prod = float(input('Digite o preço do produto: R$ '))
desc = prod - ( prod * 5 / 100)
print(f'O produto que custava R$ {prod:.2f}, na promoção com desconto de 5% vai custar R$ {desc:.2f}.')