mercado = ["tomate","alface","morango","pera", "banana"]
pesquisa = "mamão"
# Verifica se a palavra pesquisada está na lista (if in)
if pesquisa in mercado:
    print(f"'{pesquisa}' está na lista")
else:
    print(f"'{pesquisa}' não está na lista")

# Verifica se a palavra pesquisada não está na lista (if not in)
if pesquisa not in mercado:
    print(f"'{pesquisa}' não está na lista")
else:
    print(f"'{pesquisa}' está na lista") 

# Verifica se a palavra pesquisada está na lista (for in)
lista_compara = []
for item in mercado:
    if item == pesquisa:
        lista_compara.append(True)
    else:
        lista_compara.append(False)
if any(lista_compara):
    print(f"'{pesquisa}' está na lista")  
else:
    print(f"'{pesquisa}' não está na lista")  