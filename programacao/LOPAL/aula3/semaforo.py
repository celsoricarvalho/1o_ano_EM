print("--- SISTEMA DE SEMÁFORO ---")
cor = input("Qual a cor do semáforo? (verde/amarelo/vermelho): ").lower()

if cor == "verde":
    print("Siga em frente!")
elif cor == "amarelo":
    print("Atenção! Reduza a velocidade.")
elif cor == "vermelho":
    print("Pare o veículo imediatamente.")
else:
    print("Cor inválida. O semáforo deve estar quebrado!")