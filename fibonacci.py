def fibonacci(n):
    """Computes and returns the Fibonacci of n,
    a positive integer.
    """
    if n == 1: # first base case
        return 1
    elif n == 2: # second base case
        return 1
    else: # Recursive step
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))