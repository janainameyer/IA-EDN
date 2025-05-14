
'''
9 - Solicite ao usuário números inteiros até que ele digite "0". 
Armazene os positivos e negativos separadamente em duas listas. 
Ignore valores não inteiros com try/except. 
No final, mostre quantos positivos e negativos foram inseridos.
'''

positivos = []
negativos = []

while True:
    entrada = input("Digite um número inteiro (0 para sair): ")
    if entrada == '0':
        break
    try:
        num = int(entrada)
        if num > 0:
            positivos.append(num)
        elif num < 0:
            negativos.append(num)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print(f"Números positivos inseridos: {len(positivos)}")
print(f"Números negativos inseridos: {len(negativos)}")
