def adding(num1, num2):
    return num1 + num2

def dividing(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Can't divide by 0"

def sign(num1, num2, sign):
    if sign == "+":
        return adding(num1, num2)
    elif sign == '/':
        return dividing(num1, num2)
