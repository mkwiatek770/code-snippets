import time
import multiprocessing as mp


def divisors_num(number: int):
    divisors = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors += 1
    return divisors


def max_divisors_number(start: int = 1, end: int = 1000):
    best_number = start
    most_divisors = 0
    for n in range(start, end + 1):
        divisors = divisors_num(n)
        if divisors > most_divisors:
            best_number = n
            most_divisors = divisors
    return best_number, most_divisors


def no_multiprocess():
    start = time.time()
    max_num, divisors = max_divisors_number(1, 100000)
    print(f"Max number: {max_num} with {divisors} divisors")
    end = time.time()
    print(f"Time consumed: {end-start:.4f}")


def multiprocess():
    start = time.time()
    with mp.Pool(processes=5) as pool:
        chunks = [
            (1, 20000),
            (20001, 40000),
            (40001, 60000),
            (60001, 80000),
            (80001, 100000)
        ]
        results = pool.starmap(max_divisors_number, chunks)
    max_num = 0
    divisors = 0
    for num, divs in results:
        if divs > divisors:
            divisors = divs
            max_num = num
    print(f"Max number: {max_num} with {divisors} divisors")
    end = time.time()
    print(f"Time consumed: {end-start:.4f}")


if __name__ == "__main__":
    print("One process:")
    no_multiprocess()
    print("5 Processes:")
    multiprocess()
