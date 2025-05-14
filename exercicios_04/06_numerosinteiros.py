
'''
6 - Peça ao usuário que digite 10 números inteiros. 
Armazene apenas os números pares válidos em uma lista. 
Use try/except para capturar erros, continue para ignorar números ímpares ou inválidos, e exiba a lista final ao terminar.
'''

pares = []

contador = 0
while contador < 10:
    entrada = input(f"Digite o {contador + 1}º número inteiro: ")
    try:
        num = int(entrada)
        if num % 2 == 0:
            pares.append(num)
        else:
            # Número ímpar, ignorado
            continue
        contador += 1
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")
        continue

print("Números pares válidos digitados:", pares)
