#Programa que lê uma lista de 20 elementos e imprima: Moda, Mediana e Média.

a=[]
soma=0
for i in range(21):
    n=int(input("Digite um valor para a lista: "))
    a.append(n)
    soma+=n

#moda
x=a[0]
for j in range(0, len(a)):
    if a[j]==a[j-1]:
        x=a[j]

        #mediana
        for k in range(len(a)-1):
            for l in range(i+1, len(a)):
                if a[i]>a[j]:
                    a[i], a[j] = a[j], a[i]
                
soma+=a[i]   
media= soma/20
moda=x
mediana=(a[9]+a[10])/2    # caso para quantidades de elementos pares
print(f" A moda dos números é: {moda}")
print(f"A média dos números é: {media}")
print(f"A mediana dos números é: {mediana}")