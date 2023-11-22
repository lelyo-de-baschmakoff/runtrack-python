def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro impossible"
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur non valide"

result_add = calcule(5, '+', 3)
result_subtract = calcule(10, '-', 4)
result_multiply = calcule(6, '*', 7)
result_divide = calcule(20, '/', 4)
result_modulo = calcule(17, '%', 5)

print("Addition:", result_add)
print("Soustraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
print("Modulo:", result_modulo)
