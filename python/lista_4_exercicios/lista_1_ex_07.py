vi = float(input('Digite seu investimento inicial: '))
tj = float(input('Digite a taxa de juros anual (em porcentagem): '))

p = float(input('Digite o periodo de investimento(em anos): '))

vf = vi + (vi * (tj/100) * p)

print(f'O valor do seu investimento depois de {p} anos, será: {vf}')