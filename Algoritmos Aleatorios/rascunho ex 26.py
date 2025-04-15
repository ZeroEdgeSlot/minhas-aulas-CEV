#digite a frase

frase = input("digite um frase: ").strip()
print()

#ex1 ( ***descoberta, consigo adicionar pesquisas dentro da string*** )

s = frase.count(input("digite a letra que procura: "))
print()
print(F'a frase possui {s} letras')
print()

#ex2 (em que posição ela começa?)

p = frase.find((input("digite a inicial da letra que procura: ")))
print()
print(F'a inicial da sua letra esta em {p}')
print()

#ex3
f = frase.find(input("digite a ultima letra que procura: "))
print()
print(f)