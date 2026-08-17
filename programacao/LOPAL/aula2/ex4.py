idade = 18
tem_cnh = True

# Para dirigir, precisa ser maior de idade E ter CNH
pode_dirigir = (idade >= 18) and (tem_cnh == True)
print(f"Pode dirigir? {pode_dirigir}")