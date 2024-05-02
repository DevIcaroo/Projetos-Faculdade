octal= (input('Digite um numero Octal: '))
if not any(bit in '012345657' for bit in octal):
    print("Entrada inválida. Por favor, digite um número octal válido.")
else:
    decimal = int(octal, 8)
    print(f"O número {octal} em decimal é {decimal}.")



    


