def bin_para_dec(num):
    return int(num, 2)
def bin_para_oct(num):
    return oct(int(num, 2))[2:]
def bin_para_hex(num):
    return hex(int(num, 2))[2:]
def dec_para_bin(num):
    return bin(int(num))[2:]
def dec_para_oct(num):
    return oct(int(num))[2:]
def dec_para_hex(num):
    return hex(int(num))[2:]
def oct_para_bin(num):
    return bin(int(num, 8))[2:]
def oct_para_dec(num):
    return int(num, 8)
def oct_para_hex(num):
    return hex(int(num, 8))[2:]
def hex_para_bin(num):
    return bin(int(num, 16))[2:]
def hex_para_dec(num):
    return int(num, 16)
def hex_para_oct(num):
    return oct(int(num, 16))[2:]

def show_menu():
    print("Escolha a base origem:")
    print("1. Binário")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")
    escolha_origem = int(input("Digite o número da opção desejada: "))
    print("Escolha a base de destino:")
    print("1. Binário")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")
    escolha_destino = int(input("Digite o número da opção desejada: "))
    num = input("Digite o número a ser convertido: ")
    return escolha_origem, escolha_destino, num

def convert_bases(escolha_origem, escolha_destino, num):
    if escolha_origem == 1:
        if escolha_destino == 1:
            return num
        elif escolha_destino == 2:
            return bin_para_oct(num)
        elif escolha_destino == 3:
            return bin_para_dec(num)
        elif escolha_destino == 4:
            return bin_para_hex(num)
    elif escolha_origem == 2:
        if escolha_destino == 1:
            return oct_para_bin(num)
        elif escolha_destino == 2:
            return num
        elif escolha_destino == 3:
            return oct_para_dec(num)
        elif escolha_destino == 4:
            return oct_para_hex(num)
    elif escolha_origem == 3:
        if escolha_destino == 1:
            return dec_para_bin(num)
        elif escolha_destino == 2:
            return dec_para_oct(num)
        elif escolha_destino == 3:
            return num
        elif escolha_destino == 4:
            return dec_para_hex(num)
    elif escolha_origem == 4:
        if escolha_destino == 1:
            return hex_para_bin(num)
        elif escolha_destino == 2:
            return hex_para_oct(num)
        elif escolha_destino == 3:
            return hex_para_dec(num)
        elif escolha_destino == 4:
            return num

def main():
    escolha_origem, escolha_destino, num = show_menu()
    result = convert_bases(escolha_origem, escolha_destino, num)
    print("Resultado:", result)

if __name__ == "__main__":
    main()