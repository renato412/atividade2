nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B", "C"]:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print("-" * 30)
print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Média: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")
print("-" * 30)
