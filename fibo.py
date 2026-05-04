def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example
print(fibonacci(5))  # [0, 1, 1, 2, 3]
