preço = float(input('Qual o preço do produto? R$'))
parcelado = preço + (preço * 17.97 / 100)
avista = preço - (preço * 10 / 100)
print('O produto custa R${:.2f}, a vista fica por R${:.2f} e se parcelar tem o juros de 17.97% que fica R${:.2f}.'.format(preço, avista, parcelado))