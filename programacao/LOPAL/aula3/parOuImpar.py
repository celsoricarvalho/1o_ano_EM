print("--- JOGO DO ÍMPAR OU PAR ---")
numero = int(input("Digite um número inteiro: "))

resto = numero % 2

if resto == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")