import random
import time


acoes_empresa_a = 17.87
acoes_empresa_b = 16.98

print('\n')
print(f'Valor das Ações')
print(f'A - Empresa A (R${acoes_empresa_a:.2f})')
print(f'B - Empresa B (R${acoes_empresa_b:.2f})')

print("\nDia 1 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)

variacao_percentual = random.uniform(-3,3)
variacao = acoes_empresa_a * (variacao_percentual / 100)
acoes_empresa_a += variacao

variacao_percentual = random.uniform(-3,3)
variacao = acoes_empresa_b * (variacao_percentual / 100)
acoes_empresa_b += variacao

print("\nValor das Ações:")
print(f"A - Empresa A (R$ {acoes_empresa_a:.2f})")
print(f"B - Empresa B (R$ {acoes_empresa_b:.2f})")


print("\nDia 2 ", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)

variacao_percentual = random.uniform(-3,3)
variacao = acoes_empresa_a * (variacao_percentual / 100)
acoes_empresa_a += variacao

variacao_percentual = random.uniform(-3,3)
variacao = acoes_empresa_b * (variacao_percentual / 100)
acoes_empresa_b += variacao

print("\nValor das Ações:")
print(f"A - Empresa A (R$ {acoes_empresa_a:.2f})")
print(f"B - Empresa B (R$ {acoes_empresa_b:.2f})")