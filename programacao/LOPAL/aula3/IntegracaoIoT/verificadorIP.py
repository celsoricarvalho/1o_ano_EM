octeto = int(input("Digite o primeiro octeto do IP (ex: 192): "))

# Duas formas de fazer, usando 'or' ou matemática direta no Python
if octeto < 0 or octeto > 255:
    print("Erro: Endereço de IP inválido. O valor deve ser entre 0 e 255.")
else:
    print("Octeto válido, prosseguindo configuração de rede...")