import variacao

acoes_empresa_a = 17.77
acoes_empresa_b = 16.88
acoes_empresa_c = 18.55

acoes_empresas = [acoes_empresa_a, acoes_empresa_b, acoes_empresa_c]
dia = 1

print('\n')
print(f'Valor das Ações')
print(f'A - Empresa A (R${acoes_empresas[0]:.2f})')
print(f'B - Empresa B (R${acoes_empresas[1]:.2f})')
print(f'C - Empresa C (R${acoes_empresas[2]:.2f})')

dia = variacao.simula_dia(dia)

acoes_empresas = variacao.simula_variacao(acoes_empresas)

print("\nValor das Ações:")
print(f'A - Empresa A (R${acoes_empresas[0]:.2f})')
print(f'B - Empresa B (R${acoes_empresas[1]:.2f})')
print(f'C - Empresa C (R${acoes_empresas[2]:.2f})')

dia = variacao.simula_dia(dia)
acoes_empresas = variacao.simula_variacao(acoes_empresas)

print("\nValor das Ações:")
print(f'A - Empresa A (R${acoes_empresas[0]:.2f})')
print(f'B - Empresa B (R${acoes_empresas[1]:.2f})')
print(f'C - Empresa C (R${acoes_empresas[2]:.2f})')


dia = variacao.simula_dia(dia)
acoes_empresas = variacao.simula_variacao(acoes_empresas)

print("\nValor das Ações:")
print(f'A - Empresa A (R${acoes_empresas[0]:.2f})')
print(f'B - Empresa B (R${acoes_empresas[1]:.2f})')
print(f'C - Empresa C (R${acoes_empresas[2]:.2f})')

dia = variacao.simula_dia(dia)
acoes_empresas = variacao.simula_variacao(acoes_empresas)

print("\nValor das Ações:")
print(f'A - Empresa A (R${acoes_empresas[0]:.2f})')
print(f'B - Empresa B (R${acoes_empresas[1]:.2f})')
print(f'C - Empresa C (R${acoes_empresas[2]:.2f})')