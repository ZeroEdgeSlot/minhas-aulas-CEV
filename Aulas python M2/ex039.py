from datetime import date

# dia atual 
atual = date.today().year

# Data de nascimento
id = int(input("qual o ano do seu nascimento:  "))

rt = atual - id  # calculos de idade
rf = rt - 18 # quantidade de tempo apos os 18 
rl = 18 - rt  # quantidade de tempo que falta 

print(f"voce nasceu em {id}, voce tem {rt} anos, em {atual}")

if rt == 18:
   print(f"voce tem que se alistar, rapido !!!!")
elif rt > 18: 
    print(f"voce ja passou do tempo de se alistar em {rf} anos ")
elif rt < 18 :
    ano = rl + atual
    print(f"voce tem {rl} anos ate se alistar em {ano}")