binario = (input('Digite um numero Binário: '))
if not any(bit in '01' for bit in binario):
    print("Entrada inválida. Por favor, digite um número binário válido.")
else:
    decimal = int(binario, 2)
    print(f"O número {binario} em decimal é {decimal}.")
