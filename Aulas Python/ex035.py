print("digite o tamanhos das retas ")

# valores das retas
a = int(input("digite o valor: "))
b = int(input("digite o valor: "))
c = int(input("digite o valor: "))

#primeiro metodo a < b + c

#segundo metodo b < a + c

#terceiro metodo c < a + b 

if a < b + c and b < a + c and c < a + b :
    print("esse segmentos PODEM um triangulo!!!")
else :
    print("esse segmento NAO PODEM formar um triangulo!!!")