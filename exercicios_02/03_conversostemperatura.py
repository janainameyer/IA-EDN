'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

# Conversor de Temperatura entre Celsius, Fahrenheit e Kelvin

def converter_temperatura(valor, origem, destino):
    """
    Converte a temperatura de uma unidade para outra.
    Parâmetros:
        valor (float): valor da temperatura a ser convertida
        origem (str): unidade de origem ('C', 'F' ou 'K')
        destino (str): unidade de destino ('C', 'F' ou 'K')
    Retorna:
        float: valor convertido
    """
    # Primeiro, converte o valor para Celsius
    if origem == 'C':
        celsius = valor
    elif origem == 'F':
        celsius = (valor - 32) * 5/9
    elif origem == 'K':
        celsius = valor - 273.15
    else:
        raise ValueError("Unidade de origem inválida. Use 'C', 'F' ou 'K'.")

    # Em seguida, converte de Celsius para a unidade de destino
    if destino == 'C':
        return celsius
    elif destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Unidade de destino inválida. Use 'C', 'F' ou 'K'.")

# Solicita ao usuário as informações necessárias
try:
    valor = float(input("Digite o valor da temperatura: "))
    origem = input("Digite a unidade de origem (C, F ou K): ").strip().upper()
    destino = input("Digite a unidade de destino (C, F ou K): ").strip().upper()

    resultado = converter_temperatura(valor, origem, destino)
    print(f"{valor}°{origem} equivale a {resultado:.2f}°{destino}")
except ValueError as e:
    print(f"Erro: {e}")

