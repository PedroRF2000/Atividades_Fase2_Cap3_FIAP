divida=float(input("Informe o valor da dívida: "))

print(f"Total:R$ {divida} Juros:R$ 0,00 Número de parcelas:1 Valor das parcelas:R$ {divida}")
for parcelas in range (3,13,3):
    if parcelas==3:
        juros=0.1
    elif parcelas==6:
        juros=0.15
    elif parcelas==9:
        juros=0.2
    elif parcelas==12:
        juros=0.25
    valorJuros=divida*juros
    valorComJuros=divida+divida*juros
    valorParcelas=valorComJuros/parcelas
    print(f"Total:R$ {valorComJuros:.2f} Juros:R$ {valorJuros:.2f} Número de parcelas:{parcelas} Valor das parcelas:R$ {valorParcelas:.2f}")
