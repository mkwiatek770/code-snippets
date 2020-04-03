import multiprocessing
import time


def do_something(seconds):
    print(f"Sleep for {seconds} seconds")
    time.sleep(seconds)
    print("Done sleeping...")


# Dumb way
process1 = multiprocessing.Process(target=do_something, args=[1])
process2 = multiprocessing.Process(target=do_something, args=[2])

process1.start()
process2.start()

process1.join()
process2.join()


# Better way
processes = []
for _ in range(3):
    p = multiprocessing.Process(target=do_something, args=[1])
    processes.append(p)
    p.start()

for process in processes:
    process.join()

