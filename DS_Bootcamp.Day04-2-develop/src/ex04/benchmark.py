#!/usr/bin/env python3

import timeit
import random
from collections import Counter

def main():
    list = [random.randint(0, 100) for _ in range(1000000)]

    
    # if my_list_to_dict(list) == (counter_list_to_dict(list)):
    #     print("Результаты подсчета совпадают!")
    # else:
    #     print("Результаты подсчета НЕ совпадают!")

    # if my_top(list) == counter_top((counter_list_to_dict(list))):
    #     print("Результаты топ-10 совпадают!")
    # else:
    #     print("Результаты топ-10 НЕ совпадают!")
    
    my_dict_time = timeit.timeit(lambda: my_list_to_dict(list),number=1)
    my_top_time = timeit.timeit(lambda: my_top(list),number=1)
    counter_dict_time = timeit.timeit(lambda: counter_list_to_dict(list),number=1)
    counter_top_time = timeit.timeit(lambda: counter_top(list),number=1)
    print(f'my function: {my_dict_time}')
    print(f'Counter: {counter_dict_time}')
    print(f'my top: {my_top_time}')
    print(f"Counter's top: {counter_top_time}")



def my_top(list):
    dict = my_list_to_dict(list)
    sorted_nums = sorted(dict.items(), key = lambda x:x[1], reverse= True)[:10]
    return sorted_nums

def my_list_to_dict(list):
    dict = {i: 0 for i in range(0,101)}
    for n in list:
        dict[n] += 1
    return dict

def counter_top(list):
    return counter_list_to_dict(list).most_common(10)

def counter_list_to_dict(list):
    return Counter(list)  


if __name__ == '__main__':
    main()


        