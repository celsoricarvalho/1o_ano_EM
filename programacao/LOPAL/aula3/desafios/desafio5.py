print("--- CALCULADORA ---")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = n1 + n2
    print(f"O resultado é: {resultado}")
elif operacao == "-":
    resultado = n1 - n2
    print(f"O resultado é: {resultado}")
elif operacao == "*":
    resultado = n1 * n2
    print(f"O resultado é: {resultado}")
elif operacao == "/":
    # Extra (Bônus): Evitar divisão por zero!
    if n2 == 0:
        print("Erro: Não é possível dividir por zero!")
    else:
        resultado = n1 / n2
        print(f"O resultado é: {resultado}")
else:
    print("Erro: Operação inválida.")