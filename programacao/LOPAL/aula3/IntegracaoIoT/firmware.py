tamanho_mb = 120
velocidade_mbps = float(input("Qual a velocidade da rede Wi-Fi (em Mbps)? "))

# Conversão de Megabits para Megabytes
taxa_mb_s = velocidade_mbps / 8
tempo_segundos = tamanho_mb / taxa_mb_s

print(f"A taxa de transferência real é de {taxa_mb_s} MB/s.")
print(f"O download do firmware IoT vai demorar {tempo_segundos:.1f} segundos.")