'''
2 - Crie um programa que solicite um número ao usuário e exiba a tabuada desse número de 1 a 10,
utilizando a estrutura de repetição for.
'''

# Solicita ao usuário um número inteiro
numero = int(input("Digite um número para ver a tabuada: "))

# Exibe a tabuada do número de 1 até 10 usando a estrutura de repetição for
print(f"\nTabuada do {numero}:")

for i in range(1, 11):  # Vai de 1 até 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Fim do programa

'''
Fim do exercício 2 – Tabuada com estrutura de repetição for
'''

