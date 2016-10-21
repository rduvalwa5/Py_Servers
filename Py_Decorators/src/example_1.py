'''
https://realpython.com/blog/python/primer-on-python-decorators/
'''
def my_decorator(some_function):
    def wrapper():
        print('In function wrapper')
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper

def just_some_function():
    print("Decorator Example One")

just_some_function = my_decorator(just_some_function)
just_some_function()

def my_decorator2(some_function):
    def wrapper():
        num = 10
        if num == 10:
            print("Yes!")
        else:
            print("No!")
        some_function()
        print("Something is happening after some_function2() is called.")
    return wrapper

def just_some_function2():
        print("Example 2")

just_some_function2 = my_decorator2(just_some_function2)
just_some_function2()