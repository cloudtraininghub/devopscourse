def fibonacci(n):
    """Generate Fibonacci series up to n terms."""
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]


# Input the number of terms
num_terms = int(input("Enter the number of terms: "))
fib_series = fibonacci(num_terms)

# Print the Fibonacci series
print(f"Fibonacci series up to {num_terms} terms:")
print(fib_series)
