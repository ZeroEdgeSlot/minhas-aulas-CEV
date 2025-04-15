n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
n3 = int(input("digite um numero: "))

print(f"os três numero são,",n1,",",n2,"e",n3)

#verificaçâo do maior numero
menor = n1

if n2 < n1 and n2 <n3 :
    menor = n2
if n3 < n1 and n3 < n2 :
    menor = n3

maior = n1 

#verificaçâo do menor numero

if n2 > n1 and n2 > n2 :
    maior = n2
if n3 > n1 and n3 > n2 :
    maior = n3

print(f'numero maior e : {maior}')
print(f'numero menos e : {menor}')