# # Decorator function with parameters
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# # Chaining decorators
# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#
#     return wrapper
#
#
# def exclamation_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result + "!"
#
#     return wrapper
#
#
# # Applying decorators to a function
# @repeat(n=3)
# @exclamation_decorator
# @uppercase_decorator
# def greet(name):
#     return f"Hello, {name}"
#
#
# # Test the decorated function
# if __name__ == "__main__":
#     name = "Alice"
#     result = greet(name)
#     print(result)  # Output: HELLO, ALICE!HELLO, ALICE!HELLO, ALICE!
#
#
# # code for testing decorator chaining
# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#
#     return inner
#
#
# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#
#     return inner
#
#
# @decor1
# @decor
# def num():
#     return 10
#
#
# print(num())


####################################################################

# def upper_d(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#
#     return inner
#
#
# def split_d(func):
#     def wrapper():
#         str2 = func()
#         return str2.split()
#
#     return wrapper
#
#
# @split_d
# @upper_d
# def ordinary():
#     return "Good Afternoon"
#
#
# print(ordinary())

#########
# @upper_d
# @split_d            # error
# def ordinary():
#     return "Good Afternoon"
#
#
# print(ordinary())

###############################################################
# def upper_d(func):
#     def inner():
#         return "first " + func() + " first "
#
#     return inner
#
#
# def split_d(func):
#     def wrapper():
#         return "second " + func() + " second "
#
#     return wrapper
#
#
# @split_d
# @upper_d
# def ordinary():
#     return "Good Afternoon"
#
#
# print(ordinary())
#

##############################################################################
# with parameters

def outer(expr):

    def parameter_d(func):
        def inner():
            return func() + expr

        return inner

    return parameter_d

def upper_d(func):
    def inner():
        x=func()
        return x.upper()
    return inner


@upper_d
@outer("yasodha")
def ordinary():
    return "hello world...."


print(ordinary())

#############################################################################
# multiple decorator functions

def parameter_dec(fun):
    def inner(*args):
        l1=[]
        l1=args[1:]
        for i in l1:
            if i==0:
                return "Give proper input!!!!"
        return fun(*args)
    return inner
@parameter_dec
def parameters_1(a,b):
    return a/b
@parameter_dec
def parameters_2(a,b,c):
    return a/b/c

print(parameters_1(10,5))
print(parameters_2(10,2,3))

#######################################################
def decorator_1(func):
    def inner_dec_1():
        x = func()
        return x + 4

    return inner_dec_1


def decorator_2(func):
    def inner_dec_2():
        y = func()
        return y * y

    return inner_dec_2


# def decorator_3(func):
#     def inner_parameters(*names, **num_sqr):
#         print([names],num_sqr[2=4])
#
#         func()
#         #print([names],num_sqr[2=4])
#     return inner_parameters()
#


@decorator_1
@decorator_2
# @decorator_3(parameters)
def number():
    print("number")

    return 10


print(number())


#################################################



@upper_d
@outer("yasodha"," bharath")
def ordinary():
    return "hello world...."


print(ordinary())


import functools
def upper_d(func):
    @functools.wraps(func)
    def inner():
        x = func() + ". Nice to meet you"
        return x.upper()
    return inner


@upper_d
def ordinary():
    return "hello world...."


print(ordinary.__name__)