import math
import threading
import time
from concurrent.futures import ThreadPoolExecutor

"-----------------------------------------------------------------------------"


def factorial_cycle(n: int):
    multi = 1
    for i in range(1, n + 1):
        multi *= i
    return multi


def run_in_threadpool_1(numbers: list):
    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        list(executor.map(factorial_cycle, numbers))

    end_time = time.time()
    print(f"Time in ThreadPoolExecutor1: {end_time - start_time:.4f} seconds")


"-----------------------------------------------------------------------------"


def factorial_math(n: int):
    return math.factorial(n)


def run_in_threadpool_2(numbers):
    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        list(executor.map(factorial_math, numbers))

    end_time = time.time()
    print(f"Time in ThreadPoolExecutor2: {end_time - start_time:.4f} seconds")


"-----------------------------------------------------------------------------"


def run_in_threads(numbers: list):
    start_time = time.time()

    threads = [threading.Thread(target=factorial_math, args=(num,)) for num in numbers]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Execution time with threads: {end_time - start_time:.4f} seconds")


"-----------------------------------------------------------------------------"

if __name__ == "__main__":
    numbers = [100000]
    print("---------------------------------------------")
    run_in_threads(numbers)
    print("---------------------------------------------")
    run_in_threadpool_1(numbers)
    print("---------------------------------------------")
    run_in_threadpool_2(numbers)
    print("---------------------------------------------")
