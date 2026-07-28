def validate_positive(func):
    def wr(*args):
        for a in args:
            if not isinstance(a, int) or a <= 0:
                print("Error: all arguments must be positive integers.")
                return
        return func(*args)
    return wr
@validate_positive
def add(a, b):
    print("Sum:", a + b)
add(5, 3)    
add(-2, 4)    