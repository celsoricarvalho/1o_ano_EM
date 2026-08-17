# 1. Entrada de dados com conversão para decimal (float)
reais = float(input("Quanto você tem em Reais? R$: "))

# 2. Cálculos (Processamento)
dolares = reais / 5.00
euros = reais / 5.40

# 3. Saída de dados limitando a 2 casas decimais
print("\n--- CONVERSÃO ---")
print(f"Você pode comprar U$ {dolares:.2f} Dólares.")
print(f"Você pode comprar € {euros:.2f} Euros.")