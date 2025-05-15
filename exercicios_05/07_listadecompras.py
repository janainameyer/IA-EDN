
'''
7 - Crie um programa que permita ao usuário montar uma lista de compras. 
O usuário poderá adicionar itens até digitar "fim". 
Ao final, o programa exibirá todos os itens da lista. 
O programa deve estar estruturado com uma função main() 
e ser executado com if __name__ == "__main__":
'''

def main():
    lista = []
    print("Digite os itens da sua lista de compras (digite 'fim' para encerrar):")
    while True:
        item = input("Item: ")
        if item.lower() == "fim":
            break
        lista.append(item)
    
    print("\nSua lista de compras:")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
