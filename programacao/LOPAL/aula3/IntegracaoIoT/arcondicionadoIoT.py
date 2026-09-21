print("--- SMART OFFICE ---")
presenca = int(input("Há pessoas na sala? (1-Sim / 0-Não): "))
temperatura = float(input("Qual a temperatura da sala? "))

# O Ar liga se tiver pessoa E temperatura > 24
if presenca == 1 and temperatura > 24:
    print("Comando enviado: LIGANDO Ar-Condicionado.")
else:
    print("Comando enviado: MANTENDO DESLIGADO (Modo de economia).")