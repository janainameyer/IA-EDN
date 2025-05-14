
'''
7 - Crie um programa que permita que o usuário monte uma lista de compras digitando nomes de produtos. 
O usuário pode digitar até 10 itens. 
Se digitar "fim", o programa para imediatamente (break). 
Se o item for vazio (só apertar Enter), ele é ignorado com continue. 
Use try/except para garantir que apenas strings sejam inseridas.
'''

lista_compras = []

for i in range(10):
    try:
        item = input(f"Digite o {i+1}º item da lista de compras (ou 'fim' para encerrar): ")
        if item.lower() == 'fim':
            break
        if item.strip() == '':
            # Entrada vazia, ignora
            continue
        # Só aceita se for string e não vazia
        if not isinstance(item, str):
            raise ValueError("Entrada inválida, deve ser texto.")
        lista_compras.append(item)
    except Exception as e:
        print(f"Erro: {e}. Tente novamente.")

print("Lista de compras:", lista_compras)
