print("--- LOJA VIRTUAL ---")
valor_compra = float(input("Qual o valor total da compra? R$: "))
cliente_vip = int(input("Você é cliente VIP? (1 - Sim / 0 - Não): "))

# Frete grátis se a compra for maior que 150 OU se o cliente for VIP
if valor_compra > 150.00 or cliente_vip == 1:
    print("Parabéns! Você ganhou FRETE GRÁTIS.")
else:
    print("O frete custará R$ 20,00.")