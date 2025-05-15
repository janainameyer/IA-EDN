
'''
5 - Crie um programa com uma função que cadastre alunos e suas respectivas notas.
O sistema deve:
- Solicitar o nome do aluno.
- Solicitar 3 notas válidas (entre 0 e 10).
- Armazenar os dados em um dicionário, onde a chave é o nome e o valor é uma lista de notas.
- Permitir o cadastro de vários alunos até que o usuário digite "fim".
- Exibir ao final:
    - A lista de alunos e suas médias.
    - O aluno com a maior média.
Use def para as funcionalidades e try/except para tratar entradas inválidas.
'''

def cadastrar_aluno():
    alunos = {}
    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
        if nome.lower() == "fim":
            break

        notas = []
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1} de {nome}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Digite um número válido.")
        
        alunos[nome] = notas
    return alunos

def calcular_medias(alunos):
    medias = {}
    for nome, notas in alunos.items():
        medias[nome] = sum(notas) / len(notas)
    return medias

alunos = cadastrar_aluno()
medias = calcular_medias(alunos)

print("\nMédias dos alunos:")
for nome, media in medias.items():
    print(f"{nome}: {media:.2f}")

melhor_aluno = max(medias, key=medias.get)
print(f"\nAluno com a maior média: {melhor_aluno} ({medias[melhor_aluno]:.2f})")
