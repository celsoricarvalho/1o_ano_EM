porta = int(input("Qual porta o dispositivo IoT está tentando acessar? "))

if porta == 80:
    print("Conexão Liberada: Tráfego HTTP detectado.")
elif porta == 443:
    print("Conexão Liberada: Tráfego HTTPS seguro detectado.")
elif porta == 1883:
    print("Conexão Liberada: Tráfego MQTT (IoT) detectado.")
else:
    print(f"Bloqueado: A porta {porta} não é permitida no Firewall.")