# Algoritmo de busca
def busca(lista, nome_procurado):
    for i in range(len(lista)):
        if lista[i] == nome_procurado:
            return i + 1  # Retorna a posição (iniciando em 1)
    return -1  # Não encontrou

nomes = ["Maria", "Ana", "Joao", "Pedro"]
nome_procurado = input("Qual nome você quer procurar? ")
posicao = busca(nomes, nome_procurado)

if posicao != -1:
    print(f"{nome_procurado} está na posição: {posicao}")
else:
    print("O nome não está na lista.")
