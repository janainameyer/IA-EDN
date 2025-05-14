''' 
1 - Desenvolva uma calculadora em Python que realize as quatro operações básicas 
(adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve 
ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as 
especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa
'''

while True:
    try:
        # Pede para o usuário digitar o primeiro número
        num1 = float(input("Digite o primeiro número: "))
        
        # Pede para o usuário digitar o segundo número
        num2 = float(input("Digite o segundo número: "))
        
        # Pede para o usuário escolher a operação
        operacao = input("Escolha a operação (+, -, *, /): ")
        
        # Verifica qual operação o usuário escolheu e calcula o resultado
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            # Tratamento de divisão por zero
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            resultado = num1 / num2
        else:
            # Operação inválida
            raise ValueError("Operação inválida. Use +, -, * ou /.")
        
        # Se chegou aqui, operação foi concluída com sucesso
        print(f"Resultado: {resultado}")
        break  # Encerra o loop
    
    except ValueError as e:
        # Captura erros de conversão e operação inválida
        print(f"Erro: {e}. Tente novamente.")
    
    except ZeroDivisionError as e:
        # Captura erro de divisão por zero
        print(f"Erro: {e}. Tente novamente.")
