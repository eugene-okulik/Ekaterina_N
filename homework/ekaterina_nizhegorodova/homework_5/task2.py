returned = "результат операции: 42"
number_index = returned.index(":") + 2
print(int(returned[number_index:]) + 10)

returned = "результат операции: 514"
print(int(returned[number_index:]) + 10)

returned = "результат работы программы: 9"
number_index = returned.index(":") + 2
print(int(returned[number_index:]) + 10)
