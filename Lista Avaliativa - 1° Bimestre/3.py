#Programa que calcule o imposto de renda a partir de um salário de um funcionário a partir da tabela, apresenta como resultado o valor do imposto devido, o salário bruto e o salário com desconto. 

while True:  
    salario=float(input("Digite o valor do seu salario: "))
    
    if salario<=1500:
        ir1= salario*(5/100)
        r=salario-ir1
        print(f"O salário líquido é R$ {r}")
        print(f"O valor do imposto de renda é R$ {ir1}")
    elif 1500<salario<=3000:
        ir2= salario*(8/100)
        r2=salario-ir2
        print(f"O salário líquido é R$ {r2}")
        print(f"O valor do imposto de renda é R$ {ir2}")
    elif 3000<salario<=10000:
        ir3= salario*(15/100)
        r3=salario-ir3
        print(f"O salário líquido é R$ {r3}")
        print(f"O valor do imposto de renda é R$ {ir3}")
    elif salario>=15000:
        ir4= salario*(27/100)
        r4=salario-ir4
        print(f"O salário líquido é R$ {r4}")
        print(f"O valor do imposto de renda é R$ {ir4}")
    
    print(f"O salário bruto é R$ {salario}")

    a=input("Deseja continuar? (sim ou nao)")
    if a!= "sim":
        break