''' 1 - Crie um programa que solicite ao usuário uma nota (de 0 a 10) e 
exiba uma mensagem dizendo se o aluno foi reprovado, em recuperação ou aprovado'''

# Solicita ao usuário que digite uma nota entre 0 e 10
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

# Agora vamos usar estruturas de decisão para saber se o aluno foi aprovado, está em recuperação ou foi reprovado

if nota >= 7:
    # Se a nota for maior ou igual a 7, o aluno está aprovado
    print("Aluno aprovado! 🎉")

elif nota >= 5:
    # Se a nota for maior ou igual a 5, mas menor que 7, está em recuperação
    print("Aluno em recuperação. 📚")

else:
    # Se a nota for menor que 5, o aluno foi reprovado
    print("Aluno reprovado. 😢")

# Fim do programa

