# insira o valor do produto
vi = float(input("qual e o valor do produto: "))

# o valor do desconto de 5%
vd = vi * ( 5 /100) 

# o valor juros de 8%
#vj = vi * (8 / 100)

# valor do desconto
print(f"desconto de produto e: R${vd:.2f}")

# valor do juros
#print(f"juros do produto no total: R${vj:.2f}")

# soma do desconto e do juros
print(f"o valor do desconto para pagamento a vista e R${vi - vd :.2f}")
#print(f" o valor do produto com acrescimo de juros e R${vi + vj :.2f}")

