#Estrutura sequencial

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

print("Olá", nome, "seja bem-vindo(a) ao Python! 👋")
print("Você tem", idade, "anos")
print("Você mora em", cidade)

#Estrutura de repetição
for i in range(5):
    print("Contar", i)
    
contar = 0
while contar < 5:
    print("Executar", contar)
    contar += 1

#Estrutura condicional
idade = 18
if idade > 18:
    print("Maior de idade")
elif idade < 18:
    print("Menor de idade")
else:
    print("Sei la o que voce é")
    
ida = int(input("Digite sua idade: "))
if ida >= 18:
    print("Maior de idade") 
else:
    print("Menor de idade")