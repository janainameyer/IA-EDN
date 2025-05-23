'''2- Calculadora de IMC
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve solicitar
o peso (em kg) e a altura (em metros) do usuário, calcular o IMC e fornecer a classificação de acordo 
com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"'''

# Calculadora de IMC (Índice de Massa Corporal)
# O programa solicita o peso e a altura do usuário, calcula o IMC e exibe a classificação correspondente

# Solicita o peso (em kg)
peso = float(input("Digite seu peso em kg: "))

# Solicita a altura (em metros)
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o valor do IMC com duas casas decimais
print(f"Seu IMC é: {imc:.2f}")

# Classificação com base no IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 35:
    print("Classificação: Obesidade grau 1")
elif 35 <= imc < 40:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3 (mórbida)")
