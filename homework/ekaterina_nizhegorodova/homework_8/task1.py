import random
salary = int(input("Please enter your salary: "))
bonus = bool(random.choice([True, False]))
if bonus is True:
    print(f"{salary}, {bonus} - '${int(salary + (salary * random.uniform(0.01, 1)))}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
