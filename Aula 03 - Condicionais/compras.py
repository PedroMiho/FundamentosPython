# Valor gasto pelo usuario.
# Metodo de pagamento
#   - Dinheiro/Pix = 10% desconto
#   - Credito = Valor total  

valorGasto = int(input("Digite o valor gasto: "))
print("Metodo de pagamento")
print("1 - Dinheiro/PIX")
print("2 - Credito")
metodoPagamento = input("Digite o metodo de pagamento: ")

if metodoPagamento == "1":
    valorFinal = valorGasto * 0.9
    print(f"Valor final é igual a R$ {valorFinal:.2f}")
else:
    print(f"Valor final é igual a R$ {valorGasto:.2f}")
    