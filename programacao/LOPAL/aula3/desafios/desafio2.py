ano_nascimento = int(input("Em que ano você nasceu? "))
idade = 2024 - ano_nascimento # Assumindo o ano atual como 2024

if idade >= 18:
    print(f"Você tem {idade} anos. Você é MAIOR de idade.")
else:
    print(f"Você tem {idade} anos. Você é MENOR de idade.")