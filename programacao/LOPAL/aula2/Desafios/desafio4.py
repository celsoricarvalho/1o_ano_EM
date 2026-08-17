# 1. Entrada de dados
altura = float(input("Digite a altura do visitante (em metros): "))

print("Avaliando segurança...")

# 2. Processamento Booleano
# O Python vai testar a expressão e guardar True ou False dentro da variável 'liberado'
liberado = altura >= 1.45

# 3. Saída de dados
print(f"Catraca Liberada? {liberado}")