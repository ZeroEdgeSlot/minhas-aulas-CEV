import random
a1 = input("insira o nome do primeiro aluno: ")
a2 = input("insira o nome do segundo aluno: ")
a3 = input("insira o nome do terceiro aluno: ")
a4 = input("insira o nome do quarto aluno: ")
lista_nome = [a1,a2,a3,a4]
print(f"o aluno escolhido foi",random.choice(lista_nome))