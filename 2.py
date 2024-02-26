import random
import time

user_m = int(input())
user_n = int(input())
user_min_limit = int(input())
user_max_limit = int(input())
print(user_m, user_n, user_min_limit, user_max_limit)

matrix = [[random.randint(user_min_limit, user_max_limit) for n in range(user_n)] for m in range(user_m)]
print(*matrix, sep="\n")
