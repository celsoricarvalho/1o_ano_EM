print("Sistema de Triagem de Estágio SENAI")

# 1. Múltiplas entradas com seus respectivos tipos
nome = input("Nome do candidato: ")
idade = int(input("Idade: "))
nota = float(input("Nota no teste de lógica: "))
sabe_python = int(input("Sabe Python? (1 - Sim / 0 - Não): "))

# 2. Processamento Lógico Completo
# Para o aluno passar, as 3 verificações precisam ser verdadeiras (True).
# Os parênteses não são obrigatórios, mas ajudam MUITO o aluno iniciante a ler o código.
aprovado = (idade >= 16) and (nota >= 7.0) and (sabe_python == 1)

# 3. Saída de dados
print("\n--- RESULTADO DA TRIAGEM ---")
print(f"Candidato(a): {nome}")
print(f"Aprovado(a) para a vaga? {aprovado}")