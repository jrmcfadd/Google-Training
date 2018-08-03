def fib(x):
    '''Fibonnaci Numbers : takes a number (x) and returns the resulting Fibonnaci number'''
    if x >= 2:
        answer = fib(x-1) + fib(x-2)
    else:
        return 1

    return answer


def fact(n):
    # assuming that n is a positive integer or 0
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1

sep = "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print(sep)
print("Factorials")
print(sep)
print("0! =", fact(0))
print("1! =", fact(1))
print("2! =", fact(2))
print("3! =", fact(3))
print("6! =", fact(6))
print(sep)

print(sep)
print("Fibonnaci")
print(sep)

print("Fibonnaci of -> 0 is ->  " + str(fact(0)))
print("Fibonnaci of -> 1 is ->  " + str(fact(1)))
print("Fibonnaci of -> 2 is ->  " + str(fact(2)))
print("Fibonnaci of -> 3 is ->  " + str(fact(3)))
print("Fibonnaci of -> 6 is ->  " + str(fact(6)))
print(sep)