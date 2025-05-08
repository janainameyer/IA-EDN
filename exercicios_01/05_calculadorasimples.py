# Programa de Calculadora Simples
# Este programa pede dois números e uma operação (+, -, * ou /) e exibe o resultado.

# Solicitando os dois números ao usuário (convertendo para float para aceitar decimais)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicitando a operação desejada
operacao = input("Digite a operação (+, -, * ou /): ")

# Verificando qual operação foi escolhida e calculando o resultado
if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha +, -, * ou /.")

