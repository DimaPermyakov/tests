try:
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.write(input('Enter the name: ') + '\n')
        file.write(input('Enter your age: ') + '\n')
        lst = [el for el in input('Enter your languages using \',\': ').split(',')]
        for el in lst:
            file.write(el + '|')

except FileNotFoundError:
    print('Error in opening the file')
except:
    print('Unknowingly error in opening the file')

try:
    with open('file.txt', 'r', encoding='utf-8') as file:
        name = file.readline().replace('\n', '')
        age = int(file.readline())
        data = file.readline()
        data = data.split('|')
        data = [el.strip() for el in data]
        data.pop()

except FileNotFoundError:
    print('Error in opening the file')
except:
    print('Unknowingly error in opening the file')

print(name)
print(age)
print(data)
