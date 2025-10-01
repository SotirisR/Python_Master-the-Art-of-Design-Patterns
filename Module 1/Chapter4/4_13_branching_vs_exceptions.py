def divide_with_exception(number, divisor):
    try: # use f-string
        print(f"{number} / {divisor} = {number / divisor}")
    except ZeroDivisionError:
        print("You can't divide by zero")

def divide_with_if(number, divisor):
    if divisor == 0:
        print("You can't divide by zero")
    else:
        # use f-string with format specifier to show 2 decimal places
        # Equivalent to "{:.2f}".format(number / divisor)
        print(f"{number} / {divisor} = {number / divisor:.2f}")

divide_with_exception(10, 5)
divide_with_if(23, 6)
divide_with_if(10, 0)
divide_with_exception(10, 0)
