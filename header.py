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
