import asyncio
import math
import time


def is_prime(number: int) -> bool:
    prime = True
    for n in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % n == 0:
            prime = False
            break
    return prime

async def highest_prime_below(number: int) -> int:
    print(f"Highest prime below {number}")
    highest_prime = 2
    #await asyncio.sleep(1)
    for n in range(number, 2, -1):
        if is_prime(n):
            print(n)
            return n
    return None

async def main():
    
    t0 = time.time()
    await asyncio.wait([
            highest_prime_below(100000),
            highest_prime_below(10000),
            highest_prime_below(1000)    
        ])
    t1 = time.time()
    print(f"Time took: {t1 - t0}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
