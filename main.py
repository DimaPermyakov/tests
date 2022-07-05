from header import User
from header import Matrix
from source import *
import time

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
# Check changing of the branch.
