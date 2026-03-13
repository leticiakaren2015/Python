# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 13% de aumento.

salary = float(input('what is the your salary to day? R$'))
increase = salary * 13 / 100
newsalary = salary + (salary *13/ 100)
print('you will receive 13% increase corresponding to, R${:.2f}.'.format(increase))
print('your new 2024 it will be {:.2f}'.format(newsalary))
