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
