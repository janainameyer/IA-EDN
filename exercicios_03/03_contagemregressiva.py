'''
3 - Crie um programa que faça uma contagem regressiva a partir de um número informado pelo usuário até 0.
O programa deve mostrar cada número da contagem e, ao final, exibir "FIM!".
'''

numero = int(input("Digite um número para iniciar a contagem regressiva: "))

# Faz a contagem do número até 0
for i in range(numero, -1, -1):  # começa no número, vai até -1 (para incluir o 0), de 1 em 1 para trás
    print(i)

print("FIM!")

