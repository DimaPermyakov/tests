# try:
#     with open('file.txt', 'w', encoding='utf-8') as file:
#         file.write(input('Enter the name: ') + '\n')
#         file.write(input('Enter your age: ') + '\n')
#         lst = [el for el in input('Enter your languages using \',\': ').split(',')]
#         for el in lst:
#             file.write(el + '|')
#
# except FileNotFoundError:
#     print('Error in opening the file')
# except:
#     print('Unknowingly error in opening the file')
#
# try:
#     with open('file.txt', 'r', encoding='utf-8') as file:
#         name = file.readline().replace('\n', '')
#         age = int(file.readline())
#         data = file.readline()
#         data = data.split('|')
#         data = [el.strip() for el in data]
#         data.pop()
#
# except FileNotFoundError:
#     print('Error in opening the file')
# except:
#     print('Unknowingly error in opening the file')
#
# print(name)
# print(age)
# print(data)
from random import sample


def cross_zero(using_bot=False):
    date = ['ind=' + str(el) for el in range(9)]
    elements = ['  x  ', '  0  ']
    free_elements = [int(el) for el in range(9)]
    for i in range(9):
        # Игра с ботом.
        if using_bot:
            # Ход игрока.
            if i % 2 == 0:
                print_cross_zero(date)
                index = (input('Enter the index: '))
                try:
                    for letter in index:
                        if letter.isalpha():
                            raise ValueError('Letter in the word!')

                except ValueError:
                    print('Letter in the word!')
                    i -= 1
                    continue

                index = int(index)
                if date[index] != '  x  ' and date[index] != '  0  ' and 0 <= index <= 8:
                    date[index] = elements[i % 2]
                    free_elements.pop(free_elements.index(index))

                else:
                    print('Value with this index has already created.')
                    print('repeat the input!')
                    i -= 1
                    continue

            # Ход бота.
            else:
                index_bot = sample(free_elements, 1)
                free_elements.pop(free_elements.index(index_bot[0]))
                date[index_bot[0]] = elements[i % 2]

        # Игра без бота.
        else:
            print_cross_zero(date)
            index = (input('Enter the index: '))
            if index.isalpha():
                print('Enter the number!')
                i -= 1
                continue

            index = int(index)
            if date[index] != '  x  ' and date[index] != '  0  ' and 0 <= index <= 8:
                date[index] = elements[i % 2]

            else:
                print('Value with this index has already created.')
                print('repeat the input!')
                i -= 1
                continue

        # Проверка полей.
        for el_cross_zero in elements:
            res = [] * 1
            res.append(all(map(lambda el: el == el_cross_zero, date[:3])))
            res.append(all(map(lambda el: el == el_cross_zero, date[3:6])))
            res.append(all(map(lambda el: el == el_cross_zero, date[6:])))
            if any(res):
                print_cross_zero(date)
                return f'\'{el_cross_zero.strip()}\' is winner!'

            res.clear()
            res.append(all(map(lambda el: el == el_cross_zero, date[::3])))
            res.append(all(map(lambda el: el == el_cross_zero, date[1::3])))
            res.append(all(map(lambda el: el == el_cross_zero, date[2::3])))
            if any(res):
                print_cross_zero(date)
                return f'\'{el_cross_zero.strip()}\' is winner!'
            res.clear()

            res.append(all(map(lambda el: el == el_cross_zero, date[::4])))
            res.append(all(map(lambda el: el == el_cross_zero, date[2:7:2])))
            if any(res):
                print_cross_zero(date)
                return f'\'{el_cross_zero.strip()}\' is winner!'

            res.clear()

    return 'friendship won'


def print_cross_zero(arr):
    # print('   ', arr[:3])
    # print('   ', arr[3:6])
    # print('   ', arr[6:])
    print('\n-------------------------')
    print(end='|')
    for i, el in enumerate(arr):
        print(' ' + el, end=' |')
        if i == 2 or i == 5:
            print('\n-------------------------')
            print(end='|')
    print('\n-------------------------')


print(cross_zero(using_bot=True))
