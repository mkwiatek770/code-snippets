
import threading
import time
import random


class Philosopher(threading.Thread):

    running = True

    def __init__(self, name: str, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.dining_time = 0
        self.thinking_time = 0

    def run(self):
        while self.running:
            secs = random.uniform(3, 13)
            self.thinking_time += secs
            print(f"{self.name} is now thinking")
            time.sleep(secs)
            self.dine()

    def dine(self):

        left, right = self.left_fork, self.right_fork

        while self.running:
            right.acquire(True)
            locked = left.locked()
            if not locked:
                left.acquire(True)
                break
            right.release()
        else:
            return

        self.dining()
        print(f"{self.name} leaves forks on table")
        right.release()
        left.release()

    def dining(self):
        secs = random.uniform(1, 10)
        self.dining_time += secs
        print(f"{self.name} is now dining")
        time.sleep(secs)


def main():

    forks = [threading.Lock() for _ in range(5)]
    philosopher_names = ("Diogenes", "Russel", "Einstein",
                         "Laozi", "Schopenhauer")

    philosophers = [
        Philosopher(philosopher_names[i], forks[i % 5], forks[(i+1) % 5])
        for i in range(5)
    ]

    for p in philosophers:
        p.start()

    time.sleep(100)
    print("End of dining!")
    Philosopher.running = False

    time.sleep(10)
    print("Philosopher, thinking time, dining time")
    for p in philosophers:
        print(f"{p.name}  {p.thinking_time:.2f}s  {p.dining_time:.2f}s")


main()
