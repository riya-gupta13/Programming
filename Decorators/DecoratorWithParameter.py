# so if we want our decorator fxn to hve parameter then we define another fxn and enclose dec fxn in it
def outer(param):
    def upper(func):
        def inner():
            return func() + " " + param
        return inner
    return upper


@outer("Riya")
def ordinary():
    return "good morning"


print(ordinary())
