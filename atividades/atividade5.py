nota = float(input("digite a nota do primeiro bimestre: "))
nota2 = float(input("digite a nota do segundo bimestre: "))
media = (nota + nota2) / 2

if media <= 6.0:
    print("aprovado")

elif media == 10:
    print("Aprovado com Distinção")

else:
    print("reprovado")
