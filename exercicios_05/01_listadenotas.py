
'''
1 - Crie uma função que receba uma lista de notas (valores float) e calcule a média. 
O programa principal deverá solicitar ao usuário o nome de um aluno e suas 3 notas, 
e então utilizar a função para calcular e exibir a média com duas casas decimais.
'''

def calcular_media(notas):
    return sum(notas) / len(notas)

nome = input("Digite o nome do aluno: ")
notas = []

for i in range(3):
    while True:
        try:
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Por favor, digite um número válido.")

media = calcular_media(notas)
print(f"A média de {nome} é: {media:.2f}")
