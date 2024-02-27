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


def measure_time(sort_func_: Callable[[List[List[int]]], None], matrix_: List[List[int]]):
    matrix_copy = copy.deepcopy(matrix_)
    start_time = time.time()
    sort_func_(matrix_copy)
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


def shell_sort(matrix_: List[List[int]]):
    for row in matrix_:
        last_index = len(row)
        step = len(row) // 2
        while step > 0:
            for i in range(step, last_index):
                j = i
                delta = j - step
                while delta >= 0 and row[delta] > row[j]:
                    row[delta], row[j] = row[j], row[delta]
                    j = delta
                    delta = j - step
            step //= 2


def quick_sort(matrix_: List[List[int]]):
    for row in matrix_:
        if len(row) <= 1:
            continue
        support_element = row[0]
        divided_row = [[], []]
        for i in range(1, len(row)):
            if row[i] < support_element:
                divided_row[0].append(row[i])
            else:
                divided_row[1].append(row[i])
        quick_sort(divided_row)
        row.clear()
        row.extend(divided_row[0])
        row.append(support_element)
        row.extend(divided_row[1])


def tournament_sort(matrix_: List[List[int]]):
    for row in matrix_:
        for i in range(len(row), -1, -1):
            heapify(row, len(row), i)
        for i in range(len(row) - 1, 0, -1):
            row[i], row[0] = row[0], row[i]
            heapify(row, i, 0)


def heapify(sort_nums, heap_size, root):
    champion_index = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and sort_nums[left] > sort_nums[champion_index]:
        champion_index = left
    if right < heap_size and sort_nums[right] > sort_nums[champion_index]:
        champion_index = right
    if champion_index != root:
        sort_nums[root], sort_nums[champion_index] = sort_nums[champion_index], sort_nums[root]
        heapify(sort_nums, heap_size, champion_index)


def standard_sort(matrix_: List[List[int]]):
    for row in matrix_:
        row.sort()


for sort_func in [choice_sort, insert_sort, bubble_sort, shell_sort, quick_sort, tournament_sort, standard_sort]:
    measure_time(sort_func, matrix)
