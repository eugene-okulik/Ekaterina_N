def finish_me(func):
    def wrapper(*args):
        result = func(*args)
        print("finished")
        return result
    return wrapper


@finish_me
def example(text):
    print(text)


@finish_me
def example1(text):
    return text


example('print me')
print(example1("print me"))
