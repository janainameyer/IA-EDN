
'''
5 - Crie um programa que solicite ao usuário a idade de várias pessoas. 
Armazene apenas idades válidas (entre 0 e 120) em uma lista. 
Use for, try/except, continue para ignorar entradas inválidas, e break para encerrar o programa se o usuário digitar "fim". 
No final, exiba a lista das idades válidas.
'''

idades = []

for _ in range(1000):  # loop grande, break vai interromper
    entrada = input("Digite a idade (0 a 120) ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        idade = int(entrada)
        if 0 <= idade <= 120:
            idades.append(idade)
        else:
            print("Idade inválida! Deve estar entre 0 e 120.")
            continue
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para idade.")
        continue

print("Idades válidas registradas:", idades)
