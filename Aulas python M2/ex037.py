esc = int(input("digite um numero inteiro: "))
print("escolha um numero:\n"
"[1] converter para base binario:\n"
"[2] converter para base octadecimal:\n"
"[3] converter para base hexadecimal: ")

opç = int(input("digite sua opção: "))
if opç == 1:
    print(bin(esc))
elif opç == 2:
    print(oct(esc))
elif opç == 3:
    print(hex(esc))