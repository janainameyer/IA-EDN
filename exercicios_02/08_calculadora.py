'''8- Calculadora Simples
Enunciado:
Crie um programa que simule uma calculadora simples. O usuário deve informar dois números e a 
operação desejada (+, -, *, /) e o programa deve exibir o resultado da operação.'''

# Calculadora Simples em Python

# Solicita ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que escolha a operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação escolhida
if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")


