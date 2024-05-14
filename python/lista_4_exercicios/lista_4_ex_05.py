from random import uniform

def imprime_empresas(empresas, cotacoes_empresas):
    for i in range(len(empresas)):
        print(f"Cotação empresa {empresas[i]}: {cotacoes_empresas[i]}")
    print()

def simula_variacao_uma_empresa(cotacao):
    percentual = uniform(-3,3)
    variacao = cotacao*percentual
    return cotacao + variacao

def simula_variacoes(cotacoes_empresas):
    novas_cotacoes = ['x', 'x']
    for i in range(2):
        novas_cotacoes[i] = simula_variacao_uma_empresa(cotacoes_empresas[i][-1])
    return novas_cotacoes

# main

empresas = ['A', 'B']
cotacoes_empresa_a = []
cotacoes_empresa_b = []
cotacoes_empresas = [cotacoes_empresa_a, cotacoes_empresa_b]

cotacoes_empresas[0].append(100.00)
cotacoes_empresas[1].append(80.00)

# Imprime valores iniciais
print('Valores Iniciais: ')
imprime_empresas(empresas, cotacoes_empresas)

# Calcula novas cotações e adiciona a lista
novas_cotacoes = simula_variacoes(cotacoes_empresas)
cotacoes_empresas[0].append(novas_cotacoes[0])
cotacoes_empresas[1].append(novas_cotacoes[1])

print('Nova Cotação: ')
imprime_empresas(empresas, cotacoes_empresas)
