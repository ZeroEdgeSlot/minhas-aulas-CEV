sl = float(input("digite o valor do funcionario:"))
print(f"o valor do funcionario R$ {sl}")

# novo valor com 15% a mais de salario
nv = 15 / 100
s= sl * nv

print(f"o salario sera aumentado R${s:.2f}")
print(f"o salario final dos funcionarios com os aumentos {sl + s}") 