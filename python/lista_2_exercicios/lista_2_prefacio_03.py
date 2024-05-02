# Verificando se uma letra é maior que outra 

palavra = "Icaro"
letra_maior = "d"

# Verifica se existe alguma letra maior que letra_maior (any for in)
if any(char > letra_maior for char in palavra):
    print(f"Alguma letra é maior que '{letra_maior}'.")
else:
    print(f"Nenhuma letra é maior que '{letra_maior}'.")    