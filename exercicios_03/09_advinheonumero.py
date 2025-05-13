
'''
9 - Crie um programa onde o computador escolhe um número entre 1 e 10,
e o usuário deve adivinhar qual é.
O programa continua pedindo tentativas até que o usuário acerte.
Use while, break e True para controlar o fluxo.
'''

import random

numero_secreto = random.randint(1, 10)  # escolhe um número aleatório de 1 a 10

while True:
    palpite = int(input("Tente adivinhar o número entre 1 e 10: "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou! 🎉")
        break
    else:
        print("Errado! Tente novamente.")
