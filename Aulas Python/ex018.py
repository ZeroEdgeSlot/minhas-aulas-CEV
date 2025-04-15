import math  
num =float(input("qual e o angulo: "))
seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tang = math.tan(math.radians(num))
print(f"o angulo e {num}, o seno do angulo {seno:.2f}, o cosseno do angulo {cos:.2f}, a tangente do angulo e {tang:.2f}")