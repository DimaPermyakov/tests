import time
import math  # Чтобы прочитать, жми ctrl.
from functools import wraps  # для сохранения имени и документации функций при декораторах.


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Time of work: {dt}')
        return res

    return wrapper


# Декоратор производной функции.
def decorator_differential(dx=0.001):
    """ Декоратор производной функции
    :param dx: погрешность
    :return: ссылка на декоратор проивзодной
    """

    def differential(func):
        @wraps(func)  # Для сохр докум, имени и тд.
        def wrapper(num, *args, **kwargs):
            res = (func(num + dx, *args, **kwargs) - func(num, *args, **kwargs)) / dx
            return res

        # Просто сохраняем имя и документацию настоящей функции.
        # Но 2 способ, импортировать: from functools import wraps.

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__

        return wrapper

    return differential


# recursion.
def get_files(path, depth=0):
    """ Раскрытие словаря.
    Ex.
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
    :param path: словарь.
    :param depth: глубина (пробелы при раскрытии).
    :return: path[f], т.е словарь вложенный в словарь.
    """
    for f in path:
        print(' ' * depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth + 1)
        else:
            print(' ' * (depth + 1), ' '.join(path[f]))


# recursion.
def factorial(num):
    """ Функция факториала.
    :param num: число которое возводим в факториал.
    :return: число в факториале.
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# Lambda function.
def get_filter(lst, filter_func=None):
    """
    :param lst: список
    :param filter_func: лямбда функция
    :return: новый список
    """
    if filter_func is None:
        return lst
    res = []
    for el in lst:
        if filter_func(el):
            res.append(el)
    return res


def counter(start=0):
    """ Счётчик.
    Ex.
    1. c = counter(10)
    2. print(c()).
    :param start: начальное значение.
    :return: ссылку на вложенную функцию, где изменяем start.
    """

    def step():
        nonlocal start
        start += 1
        return start

    return step


@test_time
def NOD(num1, num2):
    """Вычисляется НОД для чисел a, b по алгоритму Евклида
    :param num1: первое число
    :param num2: второе число
    :return: НОД
    """
    if num1 < num2:
        num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


@test_time
def trim_string(disk, *args, sep='\\', **kwargs):
    """
    Ex. trim_string('C:', 'Users', 'dimap', 'PycharmProjects', 'tests', sep='\\', trim=True)
    :param disk: имя диска str()
    :param args: всякие слова str()
    :param sep: разделитель
    :param kwargs: trim = False|True
    :return:
    """
    args = (disk,) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [el.strip() for el in args]

    return sep.join(args)


@decorator_differential(0.000001)
def sin_x(number):
    return math.sin(number)


def decorator_transposition(func):
    def wrapper(matr):
        matr = [[row[i] for row in matr] for i in range(len(matr[0]))]
        return matr

    return wrapper


@decorator_transposition
def transpose_the_matrix(matr):
    return matr
