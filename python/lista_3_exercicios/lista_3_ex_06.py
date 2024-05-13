import variacao

acoes_empresa_a = 17.77
acoes_empresa_b = 16.88
acoes_empresa_c = 18.55
acoes_empresa_d = 19.44
acoes_empresa_e = 15.66


acoes_empresas = [acoes_empresa_a, acoes_empresa_b, acoes_empresa_c, acoes_empresa_d, acoes_empresa_e]
dia = 1

variacao.imprime_valores(acoes_empresas)

for dia in range(1,10):
    variacao.simula_dia_investimento(dia, acoes_empresas)