import sys
sys.set_int_max_str_digits(100000)


def fibo_progression(limit=10):
    fibo = 0
    next_fibo = 1
    count_fibo = 1
    while count_fibo < limit:
        yield fibo
        new_value = fibo + next_fibo
        fibo = next_fibo
        next_fibo = new_value
        count_fibo += 1


count = 1
for number in fibo_progression(100001):
    if count == 5:
        print(number)
    if count == 200:
        print(number)
    if count == 100000:
        print(number)
        break
    count += 1
