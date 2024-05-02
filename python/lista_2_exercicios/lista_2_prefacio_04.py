# Verifica se um número é maior

numero = 87889
numero_maior = 7

numero_str = str(numero)
numero_maior_str = str(numero_maior)

# Verifica se existe algum número maior que numero_maior (any for in)
if any(char > numero_maior_str for char in numero_str):
    print(f"Algum número é maior que '{numero_maior}'.")
else:
    print(f"Nenhum número é maior que '{numero_maior}'.")