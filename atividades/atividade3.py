sexo = input("Digite 'F' para Feminino ou 'M' para Masculino: ").strip().upper()

if sexo == "F":
    print("F - Feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")
