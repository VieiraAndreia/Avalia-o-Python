# Programa que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela. Mostre uma mensagem informando o saldo médio e o valor do crédito.  

smedio=int(input("Digite o valor do seu saldo médio: "))

if 0<smedio<=200:
    p1= 0
    print(f"Seu crédito é  R$ {p1}")
elif 201<=smedio<=400:
    p2=smedio*(20/100)
    print(f"Seu crédito é  R$ {p2}")
elif 401<=smedio<=600:
    p3=smedio*(30/100)
    print(f"Seu crédito é  R$ {p3}")
else: 
    p4=smedio*(40/100)
    print(f"Seu crédito é  R$ {p4}")

print(f"Seu saldo médio é R$ {smedio} ")