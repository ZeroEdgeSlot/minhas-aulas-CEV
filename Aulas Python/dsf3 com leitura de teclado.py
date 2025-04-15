N1 = (input("digite um numero:"))
N2 = (input("digite outro numero:"))
S = N1 + N2
print(f"a soma do numero {N1} e do numero {N2} e igual a {S} ")
print("ele e um numero?", N1.isnumeric(), ", e uma letra?", N1.isalpha(),", e um digito?", N1.isdigit(),", e um titulo?",N1.istitle())
print(type(S))