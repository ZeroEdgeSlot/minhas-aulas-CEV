from random import randint
from time import sleep

print("*==*" * 6)
print("Tente Acertar O Numero")
print("*==*" * 6)

sleep(3)

N = randint(0, 5) # numero aleatorio que a maquinha ira jogar entre 0 e 5

n1 = int(input("digite um numero: ")) #o jogador tenta advinhar qual o numero da maquina

if N == n1 :
    sleep(3)
    print("voce acertou ") # caso voce acerte
else:
    sleep(3)
    print("voce errou ") # caso voce erre 

print(f"Eu pensei em um numero {N}, e voce pensou em numero {n1}") # resultado