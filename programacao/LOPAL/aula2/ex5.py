# 1. Mensagem de boas-vindas
print("Bem-vindo ao Sistema Escolar!")

# 2. Entrada de Dados
nome = input("Digite o nome do aluno: ")

# Lembre-se de converter o input (que é texto) para float (número decimal)
prova1 = float(input("Nota da Prova 1: "))
prova2 = float(input("Nota da Prova 2: "))
prova3 = float(input("Nota da Prova 3: "))
trabalho = float(input("Nota do Trabalho: "))

# 3. Processamento (Cálculos e Lógica)
# Usamos parênteses para garantir que a soma aconteça antes da divisão
media_provas = (prova1 + prova2 + prova3) / 3
media_final = (media_provas + trabalho) / 2

# O operador >= vai retornar True se for maior ou igual a 7.0, e False se for menor
status_aprovacao = media_final >= 7.0

# 4. Saída de Dados (Relatório com f-strings)
print("\n--- RELATÓRIO DO ALUNO ---")
print(f"Aluno: {nome}")
# O :.1f formata o número para ter apenas 1 casa decimal (ex: 7.5 em vez de 7.5000001)
print(f"Média Final: {media_final:.1f}")
print(f"Status de Aprovação (>=7.0): {status_aprovacao}")