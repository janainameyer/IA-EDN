'''
8 - Crie um programa que solicita a nota de avaliação de um restaurante (de 0 a 5)
e exibe a quantidade de estrelas equivalente, juntamente com uma mensagem personalizada.
Use if, elif e else para lidar com diferentes faixas de nota.
'''

nota = int(input("Avalie o restaurante de 0 a 5: "))

if nota == 5:
    print("★★★★★ - Excelente! Obrigado pela avaliação!")
elif nota == 4:
    print("★★★★☆ - Muito bom! Que bom que gostou!")
elif nota == 3:
    print("★★★☆☆ - Bom! Vamos melhorar ainda mais.")
elif nota == 2:
    print("★★☆☆☆ - Sentimos muito. Vamos trabalhar nisso.")
elif nota == 1:
    print("★☆☆☆☆ - Poxa, vamos tentar melhorar.")
elif nota == 0:
    print("☆☆☆☆☆ - Que pena! Esperamos uma nova chance.")
else:
    print("Nota inválida. Digite um número entre 0 e 5.")
