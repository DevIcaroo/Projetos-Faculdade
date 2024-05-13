import random
import time
acoes_empresas = ''

def simula_variacao_uma_empresa(valor):
    variacao_percentual = random.uniform(-3, 3)
    variacao = valor * (variacao_percentual/100)
    valor += variacao
    return valor

def simula_variacao(valores):
    for i in range(len(valores)):
        valores[i] = simula_variacao_uma_empresa(valores[i])
    return valores

def simula_dia(dia): 
    print(f"\nDia {dia} ", end="", flush=True)
    for _ in range(10):
        time.sleep(0.3)
        print(".", end="", flush=True)
    return dia + 1

def imprime_valores(acoes_empresas):
    print("\nValor das Ações:")
    for i in range(len(acoes_empresas)):
        print(f"{chr(65+i)} - Empresa {chr(65+i)} (R$ {acoes_empresas[i]:.2f})")

def simula_dia_investimento(dia, valores):
    simula_dia(dia)
    valores = simula_variacao(valores)
    imprime_valores(valores)