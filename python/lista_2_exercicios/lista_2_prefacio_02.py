# lista_2_prefacio_2.py - 
# Verificando se uma letra está em uma palavra

palavra = "Gustavo"
letra_pesquisada = "c"


# Verifica se a letra_pesquisada está na palavra (if in)
if letra_pesquisada in palavra:
    print(f"A letra '{letra_pesquisada}' está na palavra '{palavra}'.")
else:
    print(f"A letra '{letra_pesquisada}' não está na palavra '{palavra}'.")


# Verifica se a letra_pesquisada não está na palavra (if not in)
if letra_pesquisada not in palavra:
    print(f"A letra '{letra_pesquisada}' não está na palavra '{palavra}'.")
else:
    print(f"A letra '{letra_pesquisada}' está na palavra '{palavra}'.")


# Verifica se algum caractere é igual a letra_pesquisada (any for in)
if any(char == letra_pesquisada for char in palavra):
    print(f"A letra '{letra_pesquisada}' está na palavra '{palavra}'.")
else:
    print(f"A letra '{letra_pesquisada}' não está na palavra '{palavra}'.")