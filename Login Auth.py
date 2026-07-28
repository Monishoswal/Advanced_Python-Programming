logged_in = True  # change to True to test
def login_required(func):
    def wr():
        if not logged_in:
            print("Access denied. Please log in first.")
        else:
            func()
    return wr
@login_required
def dashboard():
    print("Welcome to your dashboard!")
dashboard()
