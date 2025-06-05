# Recursion 

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Factorial function using Iteration
def factorial_iterative(n):
    """Calculate the factorial of a number using iteration."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_iterative(n):
    """Calculate the nth Fibonacci number using iteration."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b