# diaria do carro, sabendo que sao R$ 60,00 o dia
d = int(input("quantos dias o carro foi alugado: "))
        
# kilometragem do carro, sabendo que R$0,15 por KM rodado
k = float(input("quantos KM o carro foi rodado: "))
         
# soma do aluguel do carro e da kilometragem rodada
ss = (d * 60) + (k * 0.15)

# resultado
print(f"o total do uso do carro foi : R${ss:.2f}")