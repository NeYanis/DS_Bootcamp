#!/usr/bin/env python3

import timeit
import sys

def main(func, count):
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    match func:
        case 'loop':
            time = timeit.timeit(lambda: usual_loop(emails), number=count)
        case 'list_comprehension':
            time = timeit.timeit(lambda: list_comp(emails), number=count)
        case 'map':
            time = timeit.timeit(lambda: map_func(emails), number=count)
        case 'filter':
            time = timeit.timeit(lambda: filter_func(emails), number=count)
        case _:
            raise ValueError(f"Incorrect function argument:{func}")
    print(time)

def usual_loop(emails):
    gmail = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmail.append(email)

def list_comp(emails):
    gmail = [email for email in emails if email.endswith('@gmail.com')]

def map_func(emails):
    gmail = list(map(lambda email: email if email.endswith('@gmail.com') else None,emails))

def filter_func(emails):
    gmail = list(filter(lambda email: email.endswith('@gmail.com'), emails))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("Incorrect number of arguments Usage: ./benchmark.py function count")
    try:
        count = int(sys.argv[2])
    except ValueError:
        print(f'Count must be integer')
        sys.exit(1)
    main(sys.argv[1], count)


        