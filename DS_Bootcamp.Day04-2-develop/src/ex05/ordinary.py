#!/usr/bin/env python3
import sys
import resource

def read_file(path):
    try:
        with open(path,'r', encoding= 'utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f'File not found: {path}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("Incorrect number of arguments Usage: ./ordinary.py file_path")
    data = read_file(sys.argv[1])
    for _ in data:
        pass
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak = usage.ru_maxrss / 1024**2
    time = usage.ru_utime + usage.ru_stime
    print(f'Peak Memory Usage = {peak} GB')
    print(f'User Mode Time + System Mode Time = {time}s')