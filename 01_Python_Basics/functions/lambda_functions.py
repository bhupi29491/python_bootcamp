sum = lambda a, b: a+b
print(sum(10, 20))  # Output: 30

def calc_factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * calc_factorial(n - 1)

print(calc_factorial(5))  # Output: 120

def calc_factorial_iterative(n):
    """Calculate the factorial of a number using an iterative approach."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(calc_factorial_iterative(3))  # Output: 6