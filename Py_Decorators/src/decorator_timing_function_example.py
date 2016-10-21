'''
this example create a decorator that times the function performance
'''

import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):    
        if not num % 2:
            num_list.append(num)
            print(num)
    listSize = len(num_list)
    print("Sum of all the numbers: " , sum(num_list) ,"size of list "  ,listSize)
    

if __name__ == '__main__': 
        print(my_function())
        
'''
    Sum of all the numbers: 49995000
    Time it took to run the function: 0.0016238689422607422
'''