import random
import time
import copy
from typing import Callable, List

user_m = int(input())
user_n = int(input())
user_min_limit = int(input())
user_max_limit = int(input())
print(user_m, user_n, user_min_limit, user_max_limit)

matrix = [[random.randint(user_min_limit, user_max_limit) for n in range(user_n)] for m in range(user_m)]
print(*matrix, sep="\n")
print("=============")


def measure_time(sort_func: Callable[[List[List[int]]], None], matrix_: List[List[int]]):
    matrix_copy = copy.deepcopy(matrix_)
    start_time = time.time()
    sort_func(matrix_copy)
    print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))


def choice_sort(matrix_: List[List[int]]):
    for row in matrix_:
        for i in range(len(row) - 1):
            min_index = i
            for i1 in range(i + 1, len(row)):
                if row[i1] < row[min_index]:
                    min_index = i1
            row[i], row[min_index] = row[min_index], row[i]


def insert_sort(matrix_: List[List[int]]):
    for row in matrix_:
        for i in range(1, len(row)):
            insert_index = i
            for i1 in range(i):
                if row[i] <= row[i1]:
                    insert_index = i1
                    break
            for i2 in range(i, insert_index, -1):
                row[i2], row[i2 - 1] = row[i2 - 1], row[i2]


def bubble_sort(matrix_: List[List[int]]):
    for row in matrix_:
        for i in range(len(row) - 1):
            for i1 in range(len(row) - i - 1):
                if row[i1] > row[i1 + 1]:
                    row[i1], row[i1 + 1] = row[i1 + 1], row[i1]


for sort_func in [choice_sort, insert_sort, bubble_sort]:
    measure_time(sort_func, matrix)
