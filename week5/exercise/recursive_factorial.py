n = int(input())

def factorial(n):
    """recursive function"""
    if n == 0:
        return 1
    else:
        return n*factorial(n - 1)

print(factorial(n))
