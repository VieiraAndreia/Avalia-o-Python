#Programa que lê as notas dos 5 exames feitos e imprima a classificação do aluno, sabendo que a média é 7.0.
# classificação: A – passou em todos os exames; B – passou em I, II e IV, mas não em III ou V; C – passou em I e II, III ou IV, mas não em V. Reprovado – outras situações. 

n1=float(input("Qual foi a sua 1° nota:"))
n2=float(input("Qual foi a sua 2° nota:"))
n3=float(input("Qual foi a sua 3° nota:"))
n4=float(input("Qual foi a sua 4° nota:"))
n5=float(input("Qual foi a sua 5° nota:"))

if n1 >= 7 and n2 >= 7 and n3 >= 7 and n4 >= 7 and n5 >= 7:
    print("Parabéns! Classificação A.")
elif n1>=7 and n3>=7 and n4>=7:
    print("Parabéns! Classificação B.")
elif (n1>=7 and n2>=7) and n3>=7 or n4>=7:
    print("Parabéns! Classificação C.")
else:
    print("Você foi reprovado!")