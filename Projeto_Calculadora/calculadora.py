print("FAZER COMPRAS NO MERCADO")
print()

def mercado(compra1,compra2,preco):
    if ope == "+" or ope == "-" or ope == "*" or ope == "/":
        if ope == "+":
            result = num1 + num2
        elif ope == "-":
            result = num1 - num2
        elif ope == "*":
            result = num1 * num2
        elif ope == "/":
            result = num1 / num2
        return f'{result:.2f}'
    else:
        return "XX Operação inválida... XX"
    
compra1 = input("Digite a sua primeira compra: ")
compra2 = input("Digite a sua primeira compra: ")
preco = float(input("Qual o preço da sua compra? "))
print(f"O resultado da sua compra no super-mercado é {mercado(compra1,compra2,preco)}")   