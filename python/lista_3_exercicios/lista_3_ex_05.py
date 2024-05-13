import variacao

acoes_empresa_a = 17.77
acoes_empresa_b = 16.88
acoes_empresa_c = 18.55

acoes_empresas = [acoes_empresa_a, acoes_empresa_b, acoes_empresa_c]
dia = 1

variacao.imprime_valores(acoes_empresas )

for dia in range(1,6):
    variacao.simula_dia_investimento(dia, acoes_empresas)