from datetime import date

ano = int(input("qual e o ano que estamos (digite 0 para usar o ano da local da maquina ): "))

# linha isolada, digite zero para usar o ano da maquina local

if ano == 0 :
    ano = date.today().year

if ano % 4 == 0 and ano % 100!=0 or ano % 400 == 0 :
    print(f"{ano}, e um bissexto")
else:
    print(f"{ano}, nao e um bissexto")