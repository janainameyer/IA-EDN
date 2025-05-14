
'''
8 - Crie um programa para registrar as temperaturas de vários dias. 
O usuário deve digitar a temperatura em graus Celsius (ex: 25.5). 
O programa continua coletando até que o usuário digite "fim" ou colete 7 temperaturas. 
Valores inválidos devem ser ignorados. 
Ao final, exiba a média das temperaturas registradas.
'''

temperaturas = []

while len(temperaturas) < 7:
    entrada = input("Digite a temperatura em °C (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        temp = float(entrada)
        temperaturas.append(temp)
    except ValueError:
        print("Valor inválido. Digite uma temperatura válida.")

if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"Média das temperaturas: {media:.2f} °C")
else:
    print("Nenhuma temperatura válida foi registrada.")
