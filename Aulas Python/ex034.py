#o valor do salario do funcionario 
s =  float(input("Qual e o salario do funcionario: "))

# para salarios acima de 1250 aumento de 10%
a1 = s *(10/100)
#para salario abaixo de 1250 aumento de 15%
a2 = s*  (15/100)

if s >= 1250.00:
    novo = a1 + s 
    print(novo)
    print("salario grande hein amigao")
else:
    novo = a2 + s
    print( novo )
    print("aumento de salario, aumento um pouco necessario")


print('quem ganha {:.2f}, agora ganha : R$ {:.2f}'.format(s, novo))