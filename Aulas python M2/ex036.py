#valor da casa que ira comprar
c = float(input('qual e o valor da casa de seu desejo? : '))

# o quanto a pessoa recebe, e quanto e 30% do seu salario
s = float(input('qual e o valor do seu salario : '))

#em quanto tempo dado em meses ela ira pagar
t = int(input('em quanto tempo ira pagar a casa: '))

if s * 0.3 > c / t :
    print(f'seu emprestimo foi aprovado, é em {t} de R$ { c / t :.2f} ')
else :
    print('seu emprestimo foi negado porque a parcela ultrapassa 30% de seus salario')