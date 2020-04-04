import math
import time
import asyncio

def timer(func):

    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        value = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"Time took: {t1-t0:.2f} seconds")
        return value
    return inner


async def find_primes_in_range(first, last):
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


async def main():
    primes1 = loop.create_task(find_primes_in_range(200_000, 1_000_000))
    primes2 = loop.create_task(find_primes_in_range(50_000, 100_000))
    primes3 = loop.create_task(find_primes_in_range(50, 1000))
    await asyncio.wait([primes1, primes2, primes3])

if __name__ == "__main__":
    t0 = time.perf_counter()
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception:
        pass
    finally:
        # is it necessary?
        loop.close()
        print(f"Time took: {time.perf_counter() - t0:.2f} seconds")
