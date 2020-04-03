"""
Find the integer in the range 1 to 100000 that has the largest number of
divisors by using mutiple threads, your program will take less time 
to do the computation when it is run on a multiprocessor computer.
At the end of the program, output the elapsed time, the integer that 
has the largest number of divisors, and the number of divisors 
that it has.

Source: http://math.hws.edu/javanotes/c12/exercises.html

For this kind of task multiprocessing module is way much better.
I can't event have helper function divisors_num using multiple threads
becouse of GIL (Global Interpreter Lock).
"""
import time
import threading
import queue


def divisors_num(number: int):
    divisors = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors += 1
    return divisors


def max_divisors_number(start: int = 1, end: int = 100000):
    best_number = start
    most_divisors = 0
    for n in range(start, end + 1):
        # divisors = divisors_num(n)
        divisors = 0
        for divisor in range(1, n + 1):
            if n % divisor == 0:
                divisors += 1
        if divisors > most_divisors:
            best_number = n
            most_divisors = divisors
    print(best_number, most_divisors)
    return best_number, most_divisors


def without_threading():
    start = time.time()
    best_number, most_divisors = max_divisors_number(1, 30000)
    print(f"Best number = {best_number} with {most_divisors} divisors.")
    end = time.time()
    print(f"Time elapsed: {end - start:.2f}")


def with_threading():
    start = time.time()

    que = queue.Queue()
    threads = [
        threading.Thread(target=max_divisors_number, args=(1, 15000)),
        threading.Thread(target=max_divisors_number, args=(15001, 30000))
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    most_divisors = 0
    best_number = 0
    while not que.empty():
        number, divisors = que.get()
        if divisors > most_divisors:
            most_divisors = divisors
            best_number = number

    print(f"Best number = {best_number} with {most_divisors} divisors.")
    end = time.time()
    print(f"Time elapsed: {end - start:.2f}")


without_threading()
with_threading()
