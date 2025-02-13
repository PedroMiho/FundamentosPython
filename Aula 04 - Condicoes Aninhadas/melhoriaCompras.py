# Valor gasto pelo usuario.
# Metodo de pagamento
#   - Dinheiro/Pix = 10% de desconto
#   - Debito = 5% de desconto
#   - Credito
#       - A vista = Valor total
#       - 2x = 5% de acrescimo - Valor de cada parcela
#       - 3x = 10% de acrescimo - Valor de cada parcela


valorGasto = int(input("Digite o valor gasto: "))
print("Metodo de pagamento")
print("1 - Dinheiro/PIX")
print("2 - Debito")
print("3 - Credito")
metodoPagamento = input("Digite o metodo de pagamento: ")

if metodoPagamento == "1":
    valorFinal = valorGasto * 0.9
    print(f"Valor final é igual a R$ {valorFinal:.2f}")
elif metodoPagamento == "2":
    valorFinal = valorGasto * 0.95
    print(f"Valor final é igual a R$ {valorFinal:.2f}")
else:
    print("Formas de parcelamento")
    print("1 - A vista")
    print("2 - 2x")
    print("3 - 3x")
    parcelamento = input("Forma de parcelamento utilizado: ")

    if parcelamento == "2":
        valorFinal = valorGasto * 1.05
        valorParcela = valorFinal / 2
        print(f"Valor final é igual a R$ {valorFinal:.2f}")
        print(f"Valor parcela é igual a R$ {valorParcela:.2f}")
    elif parcelamento == "3":    
        valorFinal = valorGasto * 1.1
        valorParcela = valorFinal / 2
        print(f"Valor parcela é igual a R$ {valorParcela:.2f}")
    else:
        print(f"Valor final é igual a R$ {valorGasto:.2f}")
