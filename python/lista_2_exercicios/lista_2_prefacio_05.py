# Convertendo um número de base (bin,oct,hex) em decimal 

entrada_b = "1110"
entrada_o = "242"
entrada_x = "68c"

decimal_b = int(entrada_b, 2)
decimal_o = int(entrada_o, 8)
decimal_x = int(entrada_x, 16)

print(f"O número {entrada_b} em decimal é {decimal_b}.")
print(f"O número {entrada_o} em decimal é {decimal_o}.")
print(f"O número {entrada_x} em decimal é {decimal_x}.")

# Convertendo números formatados em (bin,oct,hex) em decimal 
entrada_b = "0b11101010"
entrada_o = "0o12651"
entrada_x = "0x7afab"

decimal_b = int(entrada_b, 2)
decimal_o = int(entrada_o, 8)
decimal_x = int(entrada_x, 16)

print(f"O número {entrada_b} em decimal é {decimal_b}.")
print(f"O número {entrada_o} em decimal é {decimal_o}.")
print(f"O número {entrada_x} em decimal é {decimal_x}.")


# Capturando apenas alguns caracteres de uma string
print(entrada_x[0:4])
print(entrada_x[2:])
print(entrada_x[-2:])
print(entrada_x[0:-2])