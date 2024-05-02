hexadecimal = (input('Digite um numero Hexadecimal: '))
if not any(bit in '01234565789abcdef' for bit in hexadecimal):
    print("Entrada inválida. Por favor, digite um número octal válido.")
else:
    decimal = int(hexadecimal, 16)
    print(f"O número {hexadecimal} em decimal é {decimal}.")