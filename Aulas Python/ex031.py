v = float(input("qual e a d istancia da sua viagem: "))


if  v <= 200 :
    print(" Uma Longa Viagem nao acha")
    print('a viagem ira custar R$', v*0.50)
else:
    print("viagem rapida hein ")
    print(" a viagem ira custar R$", v*0.45)


print("boa viagem")