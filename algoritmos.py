# Algoritmo de busca - linear

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

# Algoritmo de busca binária
def binaria(lista, nome_procurado):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == nome_procurado:
            return meio
        elif lista[meio] < nome_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1 

numeros = [1, 3, 5, 7, 9, 11, 13, 15]
posicao = binaria(numeros, 7)

if posicao != -1:
    print("Número encontrado na posição:", posicao)
else:
    print("Número não encontrado.")


    

