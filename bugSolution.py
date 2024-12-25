def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        return 0 # Handle both a and b being zero
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(10, 0) 
print(result)

result2 = function_with_uncommon_error(0,0)
print(result2) 