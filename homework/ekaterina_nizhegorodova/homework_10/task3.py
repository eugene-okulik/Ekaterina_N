def calc_decor(func):
    def wrapper(first, second, operation):
        if second < 0 or first < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif second > first:
            operation = "/"
        result = func(first, second, operation)
        return result
    return wrapper


@calc_decor
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


print(calc(3, -6, "+"))
