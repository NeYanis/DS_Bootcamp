#!/usr/bin/env python3

import timeit

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    usual_time = timeit.timeit(lambda: usual_loop(emails), number=90000000)
    list_comp_time = timeit.timeit(lambda: list_comp(emails), number=90000000)
    map_time = timeit.timeit(lambda: map_func(emails), number=90000000)
    time = sorted([map_time, list_comp_time, usual_time])
    if time[0] == map_time:
        print ("it is better to use a map")
    elif  time[0] ==  list_comp_time:
        print ("it is better to use a list comprehension")
    else:
        print ("it is better to use a loop")
    print(f'{time[0]} vs {time[1]} vs {time[2]}')

def usual_loop(emails):
    gmail = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmail.append(email)

def list_comp(emails):
    gmail = [email for email in emails if email.endswith('@gmail.com')]

def map_func(emails):
    gmail = list(map(lambda email: email if email.endswith('@gmail.com') else None,emails))


if __name__ == '__main__':
    main()
        