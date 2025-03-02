real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.88
euro = real / 6.07
iene = real / 0.04
pesoAR = real / 0.006
bitcoin = real / 509231.02
print('Com R${:.2f} você compra US$ {:.2f} '.format(real, dolar))
print('Com R${:.2f} você compra EUR {:.2f} '.format(real, euro))
print('Com R${:.2f} você compra JPY {:.2f} '.format(real, iene))
print('Com R${:.2f} você compra ARS {:.2f} '.format(real, pesoAR))
print('Com R${:.2f} você compra BTC {:.6f} '.format(real, bitcoin))