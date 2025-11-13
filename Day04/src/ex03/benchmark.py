#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def main(func, count, n):
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    match func:
        case 'loop':
            time = timeit.timeit(lambda: usual_loop(n), number=count)
        case 'reduce':
            time = timeit.timeit(lambda: reduce_func(n), number=count)
        case _:
            raise ValueError(f"Incorrect function argument:{func}")
    print(time)

def usual_loop(n):
    total = 0
    for i in range(1, n+1):
        total += i*i

def reduce_func(n):
    total = reduce(lambda x, y: x+y*y, range(1, n+1))
    


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise ValueError("Incorrect number of arguments Usage: ./benchmark.py function count number")
    try:
        count = int(sys.argv[2])
        number = int(sys.argv[3])
    except ValueError:
        print(f'Count and number must be integer')
        sys.exit(1)
    main(sys.argv[1], count, number)


        