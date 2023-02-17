class dec:
    def __init__(self, name):
        self.name = name

    # this is a type of fxn in class tht helps to call a object as a fxn
    def __call__(self, *args, **kwargs):
        return (self.name)


# here d is an object but we are callng it as fxn, it will wrk only if u define call fxn in class
d = dec("Riya")
d()


class Decorator:
    def __init__(self, func):
        self.func = func

    # this is a type of fxn in class tht helps to call a object as a fxn
    def __call__(self, *args, **kwargs):
        str1 = self.func()
        return str1.upper()


@Decorator
def greet():
    return "good morning"


print(greet())
