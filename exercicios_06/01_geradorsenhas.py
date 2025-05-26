
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Solicita ao usuário o tamanho da senha
try:
    tamanho_senha = int(input("Informe a quantidade de caracteres da senha: "))
    if tamanho_senha <= 0:
        print("Por favor, digite um número maior que zero.")
    else:
        senha_gerada = gerar_senha(tamanho_senha)
        print(f"Senha gerada: {senha_gerada}")
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
