import random
import time
import copy

user_m = int(input())
user_n = int(input())
user_min_limit = int(input())
user_max_limit = int(input())
print(user_m, user_n, user_min_limit, user_max_limit)

matrix = [[random.randint(user_min_limit, user_max_limit) for n in range(user_n)] for m in range(user_m)]
print(*matrix, sep="\n")
print("=============")

# Сортировка выбором
matrix_copy = copy.deepcopy(matrix)
start_time = time.time()
for row in matrix_copy:
    for i in range(user_n - 1):
        min_index = i
        for i1 in range(i + 1, user_n):
            if row[i1] < row[min_index]:
                min_index = i1
        row[i], row[min_index] = row[min_index], row[i]
print(*matrix_copy, sep="\n")
print("--- {0} ms ---".format(round((time.time() - start_time)*1000)))
