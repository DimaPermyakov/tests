# 1: import math as mt - заменя слова math.func() на mt.func().
# 2: from math import pi, ceil - испортируем определённые вещи, не всё.
# 3: from math import pi as PI, ceil as around - заменяем имена
import math
from header import *
import source

# two-dimensional array.
'''
arr = []
for i in range(7):
    row = [1] * (i + 1)
    for j in range(1, i + 1):
        if i != j:
            row[j] = arr[i - 1][j - 1] + arr[i - 1][j]
    arr.append(row)
for el in arr:
    print(*el)

arr = [1, 2, 3, -5, -7, 9, 0, 13, 17]
lst = ['чётное' if num % 2 == 0 else 'нечётное' for num in arr if num > 0]
print(lst)

matrix = [[1, 0, 0, 4, 5],
          [4, 2, 6, 0, 8],
          [1, 3, 7, 0, 7]]
discharged_matrix = [x for row in matrix for x in row if x != 0]
print(discharged_matrix)
'''
# Dictionary
''' 
dictionary = {input('Введите слово на английском: '): input('Введите все слова на русском через запятую: \n').split(',')
              for i in range(2)}
for key, el in dictionary.items():
    for word in el:
        print(f'{key} - {word}')

print(dictionary)
'''
# recursion.
'''
F = {
    'C:': {
        'Python39': ['python.exe', 'python.inl'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.txt', 'mathlab.exe', 'mcc.bat']
        }
    },
    'Windows': {
        'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
    }
}
get_files(F)
print(factorial(3))'''
# lambda.
'''
sum = lambda a, b: a + b
print(sum(1, 2))
lst = [1, 2, lambda: print('Hello'), 3, 4]
lst[2]()

a = [1, 2, 3, 4, -4, -3, 24]
a = get_filter(a, lambda num: num < 0)
print(*a)
'''

# print(trim_string('C:', 'Users', 'dimap', 'PycharmProjects', 'tests', sep='\\', trim=True))
# differential for sin, using the decorator.
# source.sin_x(math.pi / 3)

# ------ 1. Чтение файлов -----------------------
"""
file = open('file.txt', encoding='utf-8')
print(file.read())
file.seek(0)  # Перенос курсора в начало файла
print(file.readline(), end='')  # Первая строка.
file.seek(0)
for line in file:
    print(line, end='')
file.close()
"""
# ------ 2. Работа с файлами. Исключ ------------
'''
try:
    # file = open('file2.txt', encoding='utf-8')

    # Лучше так. Сам закрывает файл при ошибках.
    with open('file2.txt', encoding='utf-8') as file:
        s = file.readlines()
        print(s)

    # try:
    #     s = file.readlines()
    #     print(s)
    # finally:
    #     file.close()

except FileNotFoundError:
    print('Error of a opening the file')
except:
    print("Unknowingly error")
'''
# ------ 3. Запись в файл -----------------------
'''
try:
    # 'w' - write. Запись с нуля как в С++.
    # 'a' - append - Добавляем в файл, а не записываем убрав всё содержимое.
    # 'a+' - можно Читать + Добавлять.
    with open('file.txt', 'a+', encoding='utf-8') as file:
        file.seek(0)  # Перемещаем в начало, т.к режим 'a'.ТОЛЬКО для чтения.
        file.write('hello\n')
        file.writelines(['Первая строка\n', 'Вторая строка\n    '])

except:
    print('Unknowingly error in the opening the file')

'''
# БИНАРНОЕ ОТКРЫТИЕ.
'''
import pickle

books = [
    ('Book 1', 'Book 2', 250),
    ('Book 3', 'Book 3', 260),
    ('Book 5', 'Book 6', 289)
]

with open('out.bin', 'wb') as file:
    pickle.dump(books, file)

with open('out.bin', 'rb') as file:
    all_text = pickle.load(file)
    print(*all_text)
'''

# Функция filter.
'''
lst = [1, 2, 3, 4, 5, 6, 8]

# С помощью анонимной функции.
res = filter(lambda num: num % 2 == 0, lst)
print(res)
for el in res:
    print(el, end=' ')
print()

# С помощью функции.
res2 = filter(source.is_simple, lst)
for el in res2:
    print(el, end=' ')

# Простые нечётные.
res2 = filter(lambda num: num % 2 == 0, filter(source.is_simple, lst))
'''
# Функция zip.
'''
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [10, 11, 12, 13]
lst3 = 'Hello python'
res = zip(lst1, lst2, lst3)
print(res)
print(*res, sep='\n')
print('---------------')
res = zip(lst1, lst2, lst3)
res2 = zip(*res)
print(*res2, sep='\n')
'''
# Функция Sorted. Для .sort аналогично.
'''
lst = [-1, 2, 24, -534, 53, 7]
lst_sorted = sorted(lst, key=lambda num: num % 2)
print(lst_sorted)
cities = ['Москва', 'Тверь', 'Смоленск', 'Псков']
print(sorted(cities, key=len))  # Сортрировка по длине слова.
print(sorted(cities, key=lambda word: word[-1]))  # По последей букве.
'''
