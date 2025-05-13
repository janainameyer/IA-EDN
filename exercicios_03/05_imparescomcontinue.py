
'''
5 - Crie um programa que use um loop for para imprimir apenas os números ímpares de 1 a 10,
pulando os pares com o comando continue.
'''

for numero in range(1, 11):
    if numero % 2 == 0:  # Se for par
        continue  # pula esse número e vai pro próximo
    print(numero)  # Só imprime se for ímpar
