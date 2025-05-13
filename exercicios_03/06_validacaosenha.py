'''
6 - Crie um programa que simula a validação de uma senha usando um loop while True.
O usuário tem no máximo 3 tentativas para acertar a senha correta.
Use break para encerrar o loop quando a senha for correta ou quando o número máximo de tentativas for atingido.
'''

senha_correta = "admin"
tentativas = 0

while True:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Senha correta! Bem-vindo. ✅")
        break
    elif tentativas >= 3:
        print("Número máximo de tentativas atingido. Acesso bloqueado. ❌")
        break
    else:
        print("Senha incorreta. Tente novamente.")

