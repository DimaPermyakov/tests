from accessify import private
from string import ascii_letters


class User:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def print_user(self):
        return f'У {self.__name} {self.__balance} руб.'

    def top_up_balance(self, howmany):
        self.__balance += howmany

    @property
    def user_name(self):
        return self.__name

    @user_name.setter
    def user_name(self, name):
        self.__name = name


class Matrix:
    def __init__(self, size=0):
        if size == 0:
            self.__size = int(input("Size of matrix= "))
        else:
            self.__size = size
        self.__matr = [[int(el) for el in input("el=").split()] for _ in range(self.__size)]

    def print_matrix(self):
        for el in self.__matr:
            print(*el)

    def transposition(self):
        self.__matr = [[row[i] for row in self.__matr] for i in range(len(self.__matr[0]))]
        return self.__matr


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_coord(x) and self.check_coord(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_coord(cls, num):
        return type(num) in (int, float)

    def set_coord(self, x, y):
        if self.check_coord(x) and self.check_coord(y):
            self.__x = x
            self.__y = y

        else:
            raise ValueError('waited int or float')

    def get_coord(self):
        return self.__x, self.__y


'''
class Person:
    def __init__(self, inf_name='', inf_old=0):
        self.__name = inf_name
        self.__old = inf_old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, inf_old):
        if 0 < inf_old < 150:
            self.__old = inf_old
        else:
            raise ValueError('Неверный формат данных')

    @old.deleter
    def old(self):
        del self.__old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, inf_name):
        for el in inf_name:
            if not el.isalpha():
                raise ValueError(f'Обнуружен неизвестный символ: {el}')

        self.__name = inf_name

    @name.deleter
    def name(self):
        del self.__name
'''


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, inf_fio, inf_old, inf_passport, inf_weight):
        # Проверки. Можно не прописывать, т.к есть setter.
        # self.__verify_fio(inf_fio)
        # self.__verify_old(inf_old)
        # self.__verify_weight(inf_weight)
        # self.__verify_passport(inf_passport)

        self.fio = inf_fio.split()
        self.old = inf_old
        self.passport = inf_passport
        self.weight = inf_weight

    # Проверка имени.
    @classmethod
    def __verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('Fio must be string!')
        f = fio.split()

        if len(f) != 3:
            raise TypeError('format isn\'t right fio')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('')
            # Удаляем все буквы из слова, и если остался какой-то символ => он запрещён.
            if len(s.strip(letters)) != 0:
                raise TypeError('Можно использовать только буквы!')

    @classmethod
    def __verify_old(cls, old):
        if type(old) != int:
            raise TypeError('Ожидается int()!')

        if 120 < old < 0:
            raise TypeError('Диапозон [0, 120]')

    @classmethod
    def __verify_weight(cls, weight):
        if type(weight) != int and type(weight) != float:
            raise TypeError('Ожидается int()\\float()!')

        if weight < 0:
            raise TypeError('Диапозон > 0')

    @classmethod
    def __verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError('Ожидается str()!')

        # xxxx_xxxxxx
        f = passport.split()
        if len(f) != 2 or len(f[0]) != 4 or len(f[1]) != 6:
            raise TypeError('неверный формат паспорта!')

        for s in f:
            if not s.isdigit():
                raise TypeError('Должно быть число')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, new_fio):
        self.__verify_fio(new_fio)
        self.__fio = new_fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        self.__verify_old(new_old)
        self.__old = new_old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__verify_weight(new_weight)
        self.__weight = new_weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, new_passport):
        self.__verify_passport(new_passport)
        self.__passport = new_passport
