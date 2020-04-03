import multiprocessing
from concurrent import futures
import time


def do_something(seconds):
    print(f"Sleep for {seconds} seconds")
    time.sleep(seconds)
    return "Done sleeping"


with futures.ProcessPoolExecutor() as executor:
    # future1 = executor.submit(do_something, 1)
    # future2 = executor.submit(do_something, 2)
    # print(future1.result())
    # print(future2.result())

    results = [executor.submit(do_something, 1) for _ in range(10)]
    results += [executor.submit(do_something, 'a')]

    for f in futures.as_completed(results):
        # possible exceptions will be raised here
        try:
            print(f.result())
        except TypeError:
            print("exception")

with futures.ProcessPoolExecutor() as executor:
    results = executor.map(do_something, [1, 2, 3, 3, 2, 1])

    for result in results:
        print(result)
