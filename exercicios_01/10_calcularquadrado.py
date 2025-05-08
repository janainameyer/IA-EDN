# Programa para Calcular o Quadrado de um Número
# Este programa define uma função que recebe um número como argumento e retorna o quadrado desse número.

# Definindo a função para calcular o quadrado
def calcular_quadrado(numero):
    return numero ** 2

# Solicitando ao usuário que digite um número e convertendo para float
numero_usuario = float(input("Digite um número: "))

# Chamando a função para calcular o quadrado do número
resultado = calcular_quadrado(numero_usuario)

# Exibindo o resultado
print(f"O quadrado de {numero_usuario} é: {resultado}")

