# Programa para Calcular o Dobro de um Número
# Este programa define uma função que recebe um número e retorna o dobro dele.

# Definindo a função que calcula o dobro
def calcular_dobro(numero):
    return numero * 2

# Solicitando um número ao usuário e convertendo para inteiro
num = int(input("Digite um número: "))

# Chamando a função com o número fornecido pelo usuário
resultado = calcular_dobro(num)

# Exibindo o resultado na tela
print("O dobro de", num, "é:", resultado)

