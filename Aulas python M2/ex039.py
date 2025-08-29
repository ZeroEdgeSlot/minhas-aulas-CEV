import time
from datetime import date

idade = int(input("qual o ano do seu nascimento? ")) # idade do candidato
atual = date.today().year # Ano atual da candidatura

tl = atual - idade 

if idade == 18 or idade > 18:
    print(f"ja passou da hora ou ja esta na hora de se alistar")
else idade =< 18 :
    print(f"")
print(tl)