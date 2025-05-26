
import requests

def consultar_cep():
    cep = input("Informe o CEP (somente números): ").strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Deve conter exatamente 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("\n=== Endereço Encontrado ===")
            print("Logradouro:", dados.get("logradouro", "N/A"))
            print("Bairro    :", dados.get("bairro", "N/A"))
            print("Cidade    :", dados.get("localidade", "N/A"))
            print("Estado    :", dados.get("uf", "N/A"))
    else:
        print(f"Erro ao consultar o CEP. Código de status: {resposta.status_code}")

consultar_cep()
