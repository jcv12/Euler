def fibonacci_sum_even(max_value):
    a, b = 1, 2
    fib_sum = 0
    while a <= max_value:
        if a % 2 == 0:
            fib_sum += a
        a, b = b, a + b
    return fib_sum

# Example usage
print(fibonacci_sum_even(4000000))