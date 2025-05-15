
'''
3 - Crie uma função que calcule a idade de uma pessoa em dias, 
com base no ano de nascimento informado pelo usuário.
O programa deve considerar o ano atual como base para o cálculo.
Use try/except para tratar erros de entrada e valide que o ano 
não pode ser maior que o ano atual.
'''

from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    return (ano_atual - ano_nascimento) * 365

try:
    ano = int(input("Digite seu ano de nascimento: "))
    ano_atual = date.today().year
    if ano > ano_atual:
        print("O ano de nascimento não pode ser maior que o ano atual.")
    else:
        dias = idade_em_dias(ano)
        print(f"Sua idade aproximada em dias é: {dias} dias.")
except ValueError:
    print("Por favor, insira um ano válido.")
