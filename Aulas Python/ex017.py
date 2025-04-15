#import math

# cateto oposto
#co = float(input("qual e o cateto oposto: "))

# cateto adjascente
#ca = float(input("qual e o adjascente: "))

# hipotenusa
#hi = pow(co,2) + pow(ca,2)

#print(f"o hipotenusa e {math.sqrt(hi):.2f}")

#outro metodo
import math
co = float(input("qual e o cateto oposto: "))
ca = float(input("qual e o valor do cateto adjascente: "))
hip=math.hypot(co,ca)
print(f"o valor da hipotenusa e {hip:.2f}")