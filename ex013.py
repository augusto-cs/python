salário = float(input('Qual é o salário do Funcionário? R$'))
aumento = salário + (salário * 15 / 100)
print('Um Funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber {:.2f}.'.format(salário, aumento))

