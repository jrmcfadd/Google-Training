def fact(n):
    # assuming that n is a positive integer or 0
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1

print("0! =", fact(0))
print("1! =", fact(1))
print("2! =", fact(2))
print("3! =", fact(3))
print("6! =", fact(6))
