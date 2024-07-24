#Programa que cria uma lista de duas dimensões com list comprehesion e imprima a diagonal principal da lista.

a = [[int(input(f"Digite um número: ")) for j in range(3)] for i in range(3)]
dp=[]
for  i in range (3):
    for j in range (3): 
        if i==j:
            d=a[i][j]
            dp.append(d)
                    
print(f"Diagonal Principal: {dp}")