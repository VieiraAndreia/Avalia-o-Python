# Programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

dias=int(input("Quantos dias você passou com o carro alugado? "))
km=float(input(f"Quantos quilômetros foram percorridos durante esses {dias} dias?" ))

c1= 90*dias
c2=0.20*km
total=c1+c2

print(f"O preço total a pagar é: R$ {total}")