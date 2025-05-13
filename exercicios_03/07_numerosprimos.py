
'''
7 - Crie um programa que percorre uma lista de números inteiros e imprime apenas os que são números primos.
Use o for para iterar, if para a verificação e continue para pular os que não são primos.
'''

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for numero in numeros:
    if numero < 2:
        continue  # 0 e 1 não são primos

    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    
    if not primo:
        continue  # pula se não for primo
    
    print(f"{numero} é primo")
