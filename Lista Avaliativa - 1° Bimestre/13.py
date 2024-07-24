# Programa que tenha como entrada dois pontos quaisquer no plano, P(x1,y1) e P(x2,y2) e escreva a distância entre eles. 

x1=int(input("Digite um valor para o 1° ponto:"))
y1=int(input("Digite um valor para o 1° ponto:"))
x2=int(input("Digite um valor para o 2° ponto:"))
y2=int(input("Digite um valor para o 2° ponto:"))

d=(((x2-x1)**2) + ((y2-y1)**2))**1/2

print(f"A distância entre {x1,y1} e {x2,y2} é {d}.")