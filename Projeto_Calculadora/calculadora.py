print("CALCULADORA")
print()

def calcular(num1,num2,ope):
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
    
numero1 = float(input("Digite o segundo número: "))
numero2 = float(input("Digite o primeiro número: "))
operacao = input("Qual a operação? ( + - * / ) ")
print(f"O resultado da conta é {calcular(numero1, numero2, operacao)}")   