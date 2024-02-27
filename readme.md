# Лабораторная работа №1
Выполнил Косенок И. И. БСТ2201

## Задание

### Задание 1
Вызвать функцию print() и передать туда строку Hello, World!

### Задание 2
Написать генератор случайных матриц(многомерных), 
который принимает опциональные параметры 
m, n, min_limit, max_limit, 
где m и n указывают размер матрицы, 
а min_lim и max_lim - минимальное и максимальное значение 
для генерируемого числа.

### Задание 3
Реализовать методы сортировки строк числовой матрицы 
в соответствии с заданием. 
Оценить время работы каждого алгоритма сортировки и 
сравнить его со временем стандартной функции сортировки. 
Испытания проводить на сгенерированных матрицах.

## Выполнение

### Задание 1
Программа приведена в файле 1.py

### Задание 2
Программа генерации матрицы представлена в файле 2.py 

    user_m = int(input())
    user_n = int(input())
    user_min_limit = int(input())
    user_max_limit = int(input())
    print(user_m, user_n, user_min_limit, user_max_limit)
    
    matrix = [[random.randint(user_min_limit, user_max_limit) for n in range(user_n)] for m in range(user_m)]
    print(*matrix, sep="\n")
    print("=============")

### Задание 3
Программа приведена в файле 2.py

#### Сортировка выбором
Берётся срез массива, 
в котором минимальный элемент переносят в самый левый угол, 
после чего срез уменьшается и цикл повторяется.

    def choice_sort(matrix_: List[List[int]]):
        for row in matrix_:
            for i in range(len(row) - 1):
                min_index = i
                for i1 in range(i + 1, len(row)):
                    if row[i1] < row[min_index]:
                        min_index = i1
                row[i], row[min_index] = row[min_index], row[i]

Время выполнения: O(n^2)

#### Сортировка вставкой
Берём срез массива слева как отсортированную часть,
изначально она состоит из одного элемента.
Берём элемент из неотсортированной части массива и вставляем 
в отсортированную, повторяем цикл

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

Время выполнения: O(n^2)

#### Сортировка обменом
Обходим массив от начала до конца, 
попутно меняя местами неотсортированные соседние элементы

    def bubble_sort(matrix_: List[List[int]]):
        for row in matrix_:
            for i in range(len(row) - 1):
                for i1 in range(len(row) - i - 1):
                    if row[i1] > row[i1 + 1]:
                        row[i1], row[i1 + 1] = row[i1 + 1], row[i1]

Время выполнения: O(n^2)

#### Сортировка Шелла
При сортировке Шелла сначала сравниваются и сортируются между собой значения, 
стоящие один от другого на некотором расстоянии d 

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

Время выполнения: O(n^2)

#### Быстрая сортировка
Выбирается опорный элемент. Массив делится на 2 части:
элементы меньшие, чем опорный и элементы, которые
больше или равны опорному. Эти 2 части сортируются аналогичным
образом, а затем объединяются

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

Время выполнения: O(n*log(n))

#### Турнирная сортировка
Преобразуем список в бинарное дерево, 
где самый большой элемент является вершиной дерева, 
и помещаем этот элемент в конец списка. 
После перестраиваем дерево и помещаем новый 
наибольший элемент перед последним элементом в списке. 
Повторяем этот алгоритм, пока все вершины дерева не 
будут удалены. 

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

Время выполнения: O(n*log(n))

## Замер времени выполнения
Для матрицы 100*100

    --- 18 ms ---
    --- 20 ms ---
    --- 35 ms ---
    --- 6 ms ---
    --- 7 ms ---
    --- 12 ms ---
    --- 0 ms ---

Для матрицы 250*250

    --- 250 ms ---
    --- 321 ms ---
    --- 477 ms ---
    --- 37 ms ---
    --- 47 ms ---
    --- 96 ms ---
    --- 4 ms ---

Для матрицы 500*500

    --- 2237 ms ---
    --- 2959 ms ---
    --- 4383 ms ---
    --- 208 ms ---
    --- 250 ms ---
    --- 469 ms ---
    --- 13 ms ---
