import random
a1 = input("digite o nome do aluno¹: ")
a2 = input("digite o nome do aluno²: ")
a3 = input("digite o nome do aluno³: ")
a4 = input("digite o nome do aluno⁴: ")
lista_aluno = [a1,a2,a3,a4]
print(f"a sequencia de alunos é ", random.sample(lista_aluno,4))