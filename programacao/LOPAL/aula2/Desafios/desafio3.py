# 1. Entrada de dados (fatias e amigos não podem ser quebrados, então usamos int)
fatias = int(input("Quantas fatias tem a pizza? "))
amigos = int(input("Quantos amigos vão comer? "))

# 2. Processamento
# Usamos // para saber a parte inteira da divisão (ex: 12 // 5 = 2)
fatias_por_amigo = fatias // amigos

# Usamos % para pegar a sobra (ex: 12 % 5 = 2)
sobra_cachorro = fatias % amigos

# 3. Saída de dados
print("\n--- DIVISÃO ---")
print(f"Cada amigo vai comer {fatias_por_amigo} fatia(s).")
print(f"Vão sobrar {sobra_cachorro} fatia(s) para o cachorro!")