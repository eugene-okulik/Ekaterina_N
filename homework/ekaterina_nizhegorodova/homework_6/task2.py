numbers = range(1, 101)
for number in numbers:
    three = number % 3
    five = number % 5
    if three == 0 and five == 0:
        number = "FuzzBuzz"
    elif three == 0:
        number = "Fuzz"
    elif five == 0:
        number = "Bazz"
    print(number)
