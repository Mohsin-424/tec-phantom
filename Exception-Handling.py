try:
    # Code that may raise an exception
    x = 1 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero is not allowed.")
finally:
    # Code that will always be executed, regardless of whether an exception occurred or not
    print("This code will always be executed.")
    