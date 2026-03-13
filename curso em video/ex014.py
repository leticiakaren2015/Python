# Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.


temperature = float(input('actual temperature in ℃: '))
fahrenheit = ((9 * temperature) / 5) + 32
print('your temperature {}℃ in fahrenheit is {}℉.'.format(temperature, fahrenheit))
