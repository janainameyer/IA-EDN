# Programa para Exibir a Capital de um País
# Este programa armazena países e suas capitais em um dicionário e mostra a capital conforme a escolha do usuário.

# Criando um dicionário com países e suas capitais
capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington, D.C.",
    "França": "Paris",
    "Alemanha": "Berlim",
    "Japão": "Tóquio"
}

# Solicitando ao usuário o nome de um país
pais = input("Digite o nome de um país: ")

# Verificando se o país existe no dicionário e mostrando a capital
if pais in capitais:
    print(f"A capital de {pais} é {capitais[pais]}.")
else:
    print("País não encontrado no dicionário.")

