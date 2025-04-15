nome = str(input("digite seu nome completo: ")).strip()

#ex2
print("seu nome em maisculo e ", nome.upper())

#ex1
print("seu nome em minusculo e", nome.lower())

#ex3
print("seu nome ao todo tem" ,len(nome.strip()) , "letras")

#ex4 (obs: a contagem da lista sempre começa a contagem com zero ou seja "wendell" = 0  "fernandes" = 1)
fatia = nome.split()
print(f"seu primeiro nome e:",fatia[0],", é primeiro nome possui:",len(fatia[0]), "letras")