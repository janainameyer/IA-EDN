# Programa para Verificar se um Número é Par ou Ímpar
# Este programa solicita um número do usuário e informa se ele é par ou ímpar.

# Solicitando um número ao usuário e convertendo para inteiro
numero = int(input("Digite um número: "))

# Verificando se o número é par ou ímpar usando o operador módulo (%)
if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
2