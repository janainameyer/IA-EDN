
'''
4 - Crie uma função que recebe dois números e retorna a soma. 
O programa deve pedir os números ao usuário, chamar a função e exibir o resultado.
'''

def somar(a, b):
    return a + b

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = somar(num1, num2)
    print(f"A soma é: {resultado}")
except ValueError:
    print("Por favor, insira números válidos.")
