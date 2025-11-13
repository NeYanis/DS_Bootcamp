#!/usr/bin/env python3

import timeit

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    usual_time = timeit.timeit(lambda: usual_loop(emails), number=9000000)
    list_comp_time = timeit.timeit(lambda: list_comp(emails), number=90000000)
    if usual_time < list_comp_time:
        print(f'it is better to use a loop \n{usual_time} vs {list_comp_time}')
    else:
        print(f'it is better to use a list comprehension \n{list_comp_time} vs {usual_time}')

    # if usual_loop(emails) == list_comp(emails):
    #     print('Результаты совпадают')
    # else:
    #     print('Результаты HE совпадают')


def usual_loop(emails):
    gmail = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmail.append(email)
    #return gmail

def list_comp(emails):
    gmail = [email for email in emails if email.endswith('@gmail.com')]
    #return gmail

if __name__ == '__main__':
    main()
        