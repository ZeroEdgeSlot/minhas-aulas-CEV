n1 = input("digite um numero entre 0 e 9999: ")

#leitura da casa das unidade
u = n1[3:4]
print(F"tem no total de {u} unidades")

#leitura da casa da dezena
d = n1[2:3]
print(f"tem no total de {d} dezenas")

#leitura da casa da centenas
c= n1[1:2]
print(f"tem no total de {c} centenas")

#leitura da casa das milenas
m = n1[0:1]
print(f"tem no total de {m} milhares ")

#resumo total
print(f"o numero tem no total {m} milhares, {c} centenas, {d} dezenas, {u} unidade.")