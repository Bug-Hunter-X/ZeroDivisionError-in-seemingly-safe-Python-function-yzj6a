def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct return statement
    elif b == 0:
        return a # Correct return statement
    else:
        return a / b

result = function_with_uncommon_error(10, 0)  # This is going to throw an error, in this case ZeroDivisionError
print(result)