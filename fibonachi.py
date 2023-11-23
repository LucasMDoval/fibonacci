
# Dictionary to store previously calculated Fibonacci numbers
fib_cache = {}

def fib(n):
    # Check if the result is already in the cache
    if n in fib_cache:
        return fib_cache[n]
    
    # Base case
    if n <= 1:
        result = n
    else:
        # Recursive case: calculate Fibonacci number and store in the cache
        result = fib(n-1) + fib(n-2)
    
    fib_cache[n] = result  # Store the result in the cache
    return result

# Test the memoized function

result_fib_6 = fib(6)


print("Fibonacci(6):", result_fib_6)


import time

# Naive recursive approach
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Memoization approach
fib_cache = {}

def fib_memo(n):
    if n in fib_cache:
        return fib_cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fib_memo(n-1) + fib_memo(n-2)
    
    fib_cache[n] = result
    return result

# Measure time for the naive approach
start_time_naive = time.time()
result_naive = fib_naive(30)  # You can adjust the value of n as needed
end_time_naive = time.time()
print(f"Naive approach result: {result_naive}")
print(f"Naive approach execution time: {end_time_naive - start_time_naive} seconds")

# Measure time for the memoization approach
start_time_memo = time.time()
result_memo = fib_memo(30)  # You can adjust the value of n as needed
end_time_memo = time.time()
print(f"Memoization approach result: {result_memo}")
print(f"Memoization approach execution time: {end_time_memo - start_time_memo} seconds")
