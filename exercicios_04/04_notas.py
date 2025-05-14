
'''
4 - Crie um programa que permita a um professor registrar as notas de uma turma. 
O programa deve continuar solicitando notas até que o professor digite 'fim'. 
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
No final, deve exibir a média da turma.
'''

notas = []

while True:
    entrada = input("Digite a nota do aluno (0 a 10) ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite uma nota válida.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
