def number(returned):
    text = returned.split()
    return int(text[-1]) + 10


print(number("результат операции: 42"))
print(number("результат операции: 54"))
print(number("результат работы программы: 209"))
print(number("результат: 2"))
