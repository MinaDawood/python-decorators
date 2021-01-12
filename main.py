from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        return 'F-I-B-O-N-A-C-C-I'
   
    return wrapper

@my_decorator
def pfib():
    return 'Fibonacci'

print(pfib())