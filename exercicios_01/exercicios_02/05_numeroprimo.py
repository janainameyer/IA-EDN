# Verificador de Número Primo

# Solicita ao usuário que insira um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é maior que 1
if numero > 1:
    # Verifica se o número é divisível por algum número entre 2 e numero-1
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        # Se o loop não encontrar nenhum divisor, o número é primo
        print(f"{numero} é um número primo.")
else:
    # Números menores ou iguais a 1 não são primos
    print(f"{numero} não é um número primo.")
