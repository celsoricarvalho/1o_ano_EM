idade = int(input("Qual sua idade? "))
peso = float(input("Qual seu peso (em kg)? "))

# Podemos usar 16 <= idade <= 69, ou o and
if (idade >= 16 and idade <= 69) and peso > 50:
    print("Apto para doar sangue!")
else:
    print("Não apto para doar no momento.")