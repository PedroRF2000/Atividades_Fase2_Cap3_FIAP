print("Escolha o tipo de investimento: \n1.CDB \n2.LCI \n3.LCA")
tipoInvestimento=int(input("Digite o tipo de investimento (1,2 ou 3): "))
valorResgatado=float(input("Informe o valor a ser resgatado: "))
tempoInvestido=int(input("Digite o número de dias que o alor permaneceu investido: "))
if tempoInvestido>720:
    imposto=valorResgatado*0.15
elif tempoInvestido>360:
    imposto=valorResgatado*0.175
elif tempoInvestido>180:
    imposto=valorResgatado*0.2
else:
    imposto=valorResgatado*0.225
print(f"O valor do imposto de renda a ser pago é: R$ {imposto:.2f}")
