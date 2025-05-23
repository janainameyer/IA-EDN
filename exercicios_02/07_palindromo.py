'''7- Verificador de Palíndromo
Enunciado:
Crie um programa que solicite uma palavra e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de
trás para frente).'''

# Verificador de Palíndromo

# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Converte a palavra para minúsculas para garantir a comparação correta
palavra = palavra.lower()

# Verifica se a palavra é igual à sua versão invertida
if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

