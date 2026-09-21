print("--- RADAR ELETRÔNICO ---")
velocidade = float(input("Qual a velocidade do carro? "))

# Explicar que os 'dois pontos' (:) e o 'recuo' (indentação) são obrigatórios
if velocidade > 80:
    print("MULTADO! Você excedeu o limite de 80km/h.")

print("Boa viagem! Dirija com segurança.")
# Se a velocidade for menor que 80, ele pula o bloco do 'if' e só dá "Boa viagem".