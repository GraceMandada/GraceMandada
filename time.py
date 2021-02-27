import time


def simple():  # simple function
    print("I am simple function")


def decorate_it(func):  # decorator function
    def newfunction():  # creating the new function
        print("This is the new line added to your simple function:")
        simple()

    return newfunction  # returning the new function


start = time.time()
new_function = decorate_it(simple)
new_function()  # calling the new function
end = time.time()
print(end - start)