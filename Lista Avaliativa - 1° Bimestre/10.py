# Programa que calcule o IMC de uma pessoa, leia o seu peso, altura e imprima na tela sua condição

peso=float(input("Digite o seu peso em kg: "))
altura=float(input("Digite a sua altura em metros: "))
imc= peso/(altura*altura)

if imc<=18.5:
    print("Você está abaixo do peso.")
elif 18.6<=imc<=24.9:
    print("Seu peso está ideal.")
elif 25.0<=imc<=29.9:
    print("Você está levemente acima do peso.")
elif 30.0<=imc<=34.9:
    print("Você está com Obesidade grau 1")
elif 35.0<=imc<=39.9:
    print("Você está com Obesidade severa")
else:
    print("Você está com Obesidade mórbida")
        
print(f"O seu IMC é {imc}.")