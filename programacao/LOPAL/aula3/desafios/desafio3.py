nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Conceito D (Reprovado)")
    