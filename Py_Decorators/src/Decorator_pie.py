'''
    https://realpython.com/blog/python/primer-on-python-decorators/
    
    Syntactic sugar!
    Python allows you to simplify the calling of decorators using the @ symbol 
    (this is called “pie” syntax).
'''
def my_decorator_pie(some_function):
    def wrapper():
        print('In my decorator pie!')
        num = 10
        if num == 10:
            print("Modifying the function with a \"Yes!\"")
        else:
            print("Modifying the function with a \"No!\"")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper

def my_deco(num):
    return num + num

if __name__ == "__main__":
    num = 3
    print(my_decorator_pie(my_deco(num)))