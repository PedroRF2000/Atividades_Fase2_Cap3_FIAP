valorCarro=float(input("Informe o valor do carro: "))

precoFinalVista=valorCarro*0.8
print(f"O preço final a vista é de R$ {precoFinalVista:.2f}")

for parcela in range(6,61,6):
    valorTotalParcelado=valorCarro+(parcela/2*valorCarro/100)
    valorParcela=valorTotalParcelado/parcela
    print(f"O preço final parcelado em {parcela}X é de R$ {valorTotalParcelado:.2f} com parcelas no de R$ {valorParcela:.2f}")