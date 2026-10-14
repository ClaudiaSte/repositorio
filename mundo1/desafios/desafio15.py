temp = float(input("Digite a temperatura em °C: "))
f = (temp * 9 / 5) + 32
k = temp + 273.15
print('A temperatura em Celsius é {:.1f}°C, em Fahrenheit é {:.1f}°F e em Kelvin é {:.1f}K.'.format(temp, f, k))