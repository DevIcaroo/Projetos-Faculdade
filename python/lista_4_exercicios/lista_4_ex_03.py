from random import uniform

def simula_variacao_uma_empresa(cotacao):
    percentual = uniform(-3,3)
    variacao = cotacao*percentual
    return cotacao + variacao
# Main

cotacoes_empresa_a = []
cotacoes_empresa_b = []

cotacoes_empresa_a.append(100.00)
cotacoes_empresa_b.append(115.00)

print()
print(f"Cotação empresa A: {cotacoes_empresa_a}")
print(f"Cotação empresa B: {cotacoes_empresa_b}")


nova_cotacao_a = simula_variacao_uma_empresa(cotacoes_empresa_a[-1])
nova_cotacao_b = simula_variacao_uma_empresa(cotacoes_empresa_b[-1])

cotacoes_empresa_a.append(nova_cotacao_a)
cotacoes_empresa_b.append(nova_cotacao_b)

print()
print(f"Cotação empresa A: {cotacoes_empresa_a}")
print(f"Cotação empresa B: {cotacoes_empresa_b}")
