import time
def log_call(func):
    def wr(*args, **kwargs):
        print(f"Calling '{func.__name__}' at {time.ctime()}")
        return func(*args, **kwargs)
    return wr
@log_call
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")