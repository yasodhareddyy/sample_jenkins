"""
Write a python program using the decorator function with parameters and
chaining decorators.

syntax: decorator parameters

@decorator(params)
def func_name():
    ''' Function implementation'''


def func_name():
    ''' Function implementation'''

func_name = (decorator(params))(func_name)
"""


def outer(expr, expr1):
    def parameter_d(func):
        def inner():
            x = func() + expr + expr1
            return x

        return inner

    return parameter_d


def upper_d(func):
    def inner():
        x = func() + ". Nice to meet you"
        return x.upper()

    return inner

@upper_d
@outer("yasodha ","bharath")
def ordinary():
    return "hello world...."


print(ordinary())


##############################################################################
def add_decorator(add):
    def decorator_1(func):
        def inner():
            x = func() + add
            return x

        return inner

    return decorator_1


def decorator_2(func):
    def inner():
        x = func() * 4
        return x

    return inner


# Using the decorators
@add_decorator(10)
@decorator_2
def number():
    return 4


print(number())

##############################################################################

class Pattern:
    def __init__(self, n):
        self.n = n

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print(self.n * '*')
            result = fn(*args, **kwargs)
            print(result)
            print(self.n * '*')
            return result

        return wrapper


@Pattern(5)
def add(a, b):
    return a + b


add(20, 30)

####################################################
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)