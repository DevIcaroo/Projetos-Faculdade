def bin_para_decimal(numero):
    return int(numero, 2)
def octal_para_decimal(numero):
    return int(numero, 8)
def hexa_para_decimal(numero):
    return int(numero, 16)

def dec_para_binario(numero):
    return bin(numero)
def dec_para_octal(numero):
    return oct(numero)
def bin_para_hexadecimal(numero):
    return hex(numero)





while True:  
    print("Escolha uma opção entre: Binario, Octal, Decimal, Hexadecimal")   
    print("1) Binario")  
    print("2) Octal")  
    print("3) Decimal")
    print("4) Hexadecimal") 
    print("0) para sair")

    escolha1 = input("Digite a letra correspondente à base numérica escolhida: ")  
    if escolha1 == '0':
        print("Programa encerrado.")
        break
    elif escolha1 not in {'1', '2', '3', '4'}:
        print("Escolha inválida.") 
        continue

    print("Agora escolha uma opção para converter o numero escolhido entre: Binario, Octal, Decimal, Hexadecimal")      
    print("1) Binario")  
    print("2) Octal")  
    print("3) Decimal")
    print("4) Hexadecimal") 
    print("0) para sair")
    escolha2 = input("Digite a letra correspondente à base numérica escolhida: ")  
    if escolha2 == '0':
        print("Programa encerrado.")
    elif escolha2 not in ['1', '2', '3', '4']:
        print("Escolha inválida.")
        continue
#main
    input('Agora escreva o numero que quer converter: ')

    if escolha1 == '1':
        numero_decimal = bin_para_decimal(escolha1)
    elif escolha1 == '2':
        numero_decimal = octal_para_decimal(escolha1)
    elif escolha1 == '3':
        int(escolha1)
