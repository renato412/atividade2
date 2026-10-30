num1 = int(input("Insira o dia: "))
num2 = int(input("Insira o mes: "))
num3 = int(input("Insira o ano: "))

if num1 <= 31 and num2 <= 12 and num3 <= 100000:
    print(f"a data {num1}/{num2}/{num3} e valida")
else:
    print("invalido")
