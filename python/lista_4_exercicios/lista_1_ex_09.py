tot = int(input('Digite o Valor da compra: '))
percentual_desc = int(input('Digite o do desconto: '))
desc = tot * (percentual_desc / 100)
vf = tot - desc

print(f'O valor da sua compra com desconto é {vf}')