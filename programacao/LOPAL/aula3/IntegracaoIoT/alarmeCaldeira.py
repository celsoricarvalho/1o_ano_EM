temperatura = float(input("Temperatura atual (°C): "))
pressao = float(input("Pressão atual (PSI): "))

if temperatura > 100 or pressao > 50:
    print("ALERTA CRÍTICO: Desligando caldeira! Risco de falha.")
else:
    print("Sistema operando normalmente.")