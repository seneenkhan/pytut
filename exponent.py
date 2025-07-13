from unittest import result


def power_func(base,exp):
    result = 1
    for index in range(exp):
        result = result * base
    return result

print(power_func(2,5))

