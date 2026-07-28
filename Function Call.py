def count_calls(func):
    def wr(*args, **kwargs):
        wr.count += 1
        print(f"'{func.__name__}' has been called {wr.count} time(s)")
        return func(*args, **kwargs)
    wr.count = 0
    return wr


@count_calls
def say_hi():
    print("Hi!")


say_hi()
say_hi()
say_hi()