while True:  
    print("Escolha uma opção entre: Binario, Octal e Hexadecimal")
    
    print("a) Binario")  
    print("b) Octal")  
    print("c) Hexadecimal")

    escolha = input("Digite a letra correspondente à base numérica escolhida: ")  
    if escolha == 'a':
        print("a) Binario") 
        binario = input('Agora que a base numérica escolhida foi binario, digite um numero para converter para decimal: ')
        if not any(bit in '01' for bit in binario):
            print("Entrada inválida. Por favor, digite um número binário válido.")
        else:
            decimal = int(binario, 2)
        print(f"O número {binario} em decimal é {decimal}.")
        r = str(input("Quer converter outro numero? [sim/não]"))
    elif escolha == 'b':
        print("b) Octal") 
        octal = input('Agora que a base numérica escolhida foi octal, Digite um numero para converter para decimal: ')
        if not any(bit in '012345657' for bit in octal):
            print("Entrada inválida. Por favor, digite um número octal válido.")
        else:
            decimal = int(octal, 8)
            print(f"O número {octal} em decimal é {decimal}.")
            r = str(input("Quer converter outro numero? [sim/não]"))
    elif escolha == 'c':
        print("c) Hexadecmial") 
        hexadecimal = input('Agora que a base numérica escolhida foi octal, digite um numero para converter para decimal: ')
        if not any(bit in '01234565789abcdef' for bit in hexadecimal):
            print("Entrada inválida. Por favor, digite um número hexadecimal válido.")
        else:
            decimal = int(hexadecimal, 16)
        print(f"O número {hexadecimal} em decimal é {decimal}.")
        r = str(input("Quer converter outro numero? [sim/não]"))
    else:
        print("Escolha inválida")
        r = str(input(" Quer tentar novamente? [sim/não]"))
        if r == "não":
            print("Programa encerrado.")
            break