# recursion.
import time


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


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Time of work: {dt}')
        return res

    return wrapper


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
