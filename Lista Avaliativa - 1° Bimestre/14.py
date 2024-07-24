# Programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

numero=int(input("Digite um número: "))
l1=[]

for i in range(1,numero):
    for j in range(2,i): 
        if i%j==0:
            break
        else: 
            l1.append(i)
print(f"Os números primos de 1 a {numero} é {l1}")