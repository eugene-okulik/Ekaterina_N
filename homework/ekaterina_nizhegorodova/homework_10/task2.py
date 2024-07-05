def repeat_me(func):
    def wrapper(*args, count):
        result = None
        for repeat in range(count):
            result = func(*args)
        return result
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
example('print me too', count=4)
