import time
import variacao


acoes_empresa_a = 17.77
acoes_empresa_b = 16.88
acoes_empresa_c = 18.55

print('\n')
print(f'Valor das Ações')
print(f'A - Empresa A (R${acoes_empresa_a:.2f})')
print(f'B - Empresa B (R${acoes_empresa_b:.2f})')
print(f'C - Empresa C (R${acoes_empresa_c:.2f})')

print("\nDia 1 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)

acoes_empresa_a = variacao.simula_variacao_uma_empresa(acoes_empresa_a)
acoes_empresa_b = variacao.simula_variacao_uma_empresa(acoes_empresa_b)
acoes_empresa_c = variacao.simula_variacao_uma_empresa(acoes_empresa_c)

print("\nValor das Ações:")
print(f"A - Empresa A (R$ {acoes_empresa_a:.2f})")
print(f"B - Empresa B (R$ {acoes_empresa_b:.2f})")
print(f'C - Empresa C (R$ {acoes_empresa_c:.2f})')


print("\nDia 2 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)

acoes_empresa_a = variacao.simula_variacao_uma_empresa(acoes_empresa_a)
acoes_empresa_b = variacao.simula_variacao_uma_empresa(acoes_empresa_b)
acoes_empresa_c = variacao.simula_variacao_uma_empresa(acoes_empresa_c)

print("\nValor das Ações:")
print(f"A - Empresa A (R$ {acoes_empresa_a:.2f})")
print(f"B - Empresa B (R$ {acoes_empresa_b:.2f})")
print(f'C - Empresa C (R$ {acoes_empresa_c:.2f})')