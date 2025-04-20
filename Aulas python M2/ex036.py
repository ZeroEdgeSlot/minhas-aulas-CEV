#valor da casa que ira comprar
c = float(input('qual e o valor da casa de seu desejo? : '))

# o quanto a pessoa recebe,
s = float(input('qual e o valor do seu salario : '))

# em quanto tempo dado em meses ela ira pagar ( tempo dado em meses )
t = int(input('em quanto tempo ira pagar a casa: '))

# contas
tp = t * 12 # quantidade de meses da parcela
ps = s * 0.3 # porcentagem do salario
vp = c / tp # valor da parcela da casa

if ps >= vp :
    print(f"voce recebe {s} e 30% do seu salario equivale {ps}")
    print(f'seu emprestimo foi aprovado, é em {tp} meses de R$ {vp:.2f} ')
else :
    print(f'seu emprestimo foi negado porque a parcela de {vp:.2f} reais em {tp} meses ultrapassa 30% {ps} de seus salario ')