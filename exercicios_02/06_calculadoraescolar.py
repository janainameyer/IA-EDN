'''6- Calculadora de Média Escolar
Enunciado:
Desenvolva um programa que solicite o nome de um aluno e suas 3 notas. O programa deve calcular a
média e informar se o aluno foi aprovado (média >= 7), está em recuperação (5 <= média < 7) ou foi
reprovado (média < 5).'''

# Calculadora de Média Escolar

# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Solicita as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média com duas casas decimais
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

# Verifica a situação do aluno com base na média
if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")

