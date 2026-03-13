#  Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

measure = float(input('write a distance in meters'))
cm = measure * 100
mm = measure * 1000
print('the value {} is equivalent {}cm end the value {} is equivalent {}mm . '.format(measure, cm, measure, mm))
