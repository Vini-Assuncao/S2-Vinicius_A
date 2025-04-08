


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
