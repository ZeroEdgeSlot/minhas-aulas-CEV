m1 = int(input("qual era a valocidade do carro? "))

print(m1, "KM por hora")

m2 = m1 - 80 

if m1 >= 80:
    print("você foi multado!!!")
    print('voce ira pagar  R$' ,m2 * 7 , 'reais de multa')
else:
    print("velocidade adequada")