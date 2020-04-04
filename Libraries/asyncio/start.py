import math
import time

def timer(func):

    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        value = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"Time took: {t1-t0:.2f}")
        return value
    return inner

@timer
def find_primes_in_range(first, last):
    primes = []
    for num in range(first, last + 1):
        is_prime = True
        for divisor in range(2, math.ceil(math.sqrt(num)) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(f"Found {len(primes)} primes in range from {first} to {last}")
    return primes

if __name__ == "__main__":
    find_primes_in_range(200_000, 1_000_000)
    find_primes_in_range(50_000, 100_000)
    find_primes_in_range(50, 1000)
