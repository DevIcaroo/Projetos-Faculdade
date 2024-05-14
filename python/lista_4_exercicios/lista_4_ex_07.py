from random import uniform

def imprime_empresas(empresas, cotacoes_empresas):
    for i in range(len(empresas)):
        print(f'Cotação empresa {empresas[i]}: {cotacoes_empresas[i]}')
    print()

def simula_variacao_uma_empresa(cotacao):
    percentual = uniform(-3,3)
    variacao = cotacao*percentual
    return cotacao + variacao

def simula_variacoes(cotacoes_empresas):
    novas_cotacoes = ['', '']
    for i in range(2):
        novas_cotacoes[i] = simula_variacao_uma_empresa(cotacoes_empresas[i][-1])
        cotacoes_empresas[i].append(novas_cotacoes[i])

        print()
        print(f'Cotação empresa {empresas[i]}: ') 
        print([f"{valor:.2f}" for valor in cotacoes_empresas[i]])
# main

empresas = ['A', 'B']
cotacoes_empresa_a = []
cotacoes_empresa_b = []
cotacoes_empresas = [cotacoes_empresa_a, cotacoes_empresa_b]

cotacoes_empresas[0].append(100.00)
cotacoes_empresas[1].append(80.00)

# print('Valores Iniciais: ')
# imprime_empresas(empresas, cotacoes_empresas)

# Calcula novas cotações e adiciona a lista
simula_variacoes(cotacoes_empresas)

# print('Nova Cotação: ')
# imprime_empresas(empresas, cotacoes_empresas)
