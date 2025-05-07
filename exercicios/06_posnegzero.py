# Programa para Verificar se um Número é Positivo, Negativo ou Zero
# Este programa pede um número ao usuário e informa se ele é positivo, negativo ou igual a zero.

# Solicitando o número ao usuário e convertendo para float (para aceitar decimais)
numero = float(input("Digite um número: "))

# Verificando se o número é positivo, negativo ou zero
if numero > 0:
    print("O número", numero, "é positivo.")
elif numero < 0:
    print("O número", numero, "é negativo.")
else:
    print("O número é zero.")

