def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


def str_split(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper


@str_split
@str_upper
def ordinary():
    return "good morning"


print(ordinary())
