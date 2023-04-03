c1 = int(input('Введите кол-во элементов для 1-го множества: '))
first = set(input()for i in range(c1))

c2 = int(input('Введите кол-во элементов для 2-го множества: '))
second = set(input() for i in range(c2))

start = int(input('Введите 1, если хотите начать изменять множества, иначе 0: '))
while start == 1:
    num = int(input('Если хотите изменить множество, введите его номер: '))
    if num == 1:
        oper = int(input(
            'Введите 1, если хотите добавить в множество:  \n ''введите 2, если хотите удалить элемент из множества: \n'
            ' Введите 0, если ничего не хотите менять: \n '))
        while oper != 0:
            if oper == 1:
                count_add = int(input('Введите кол-во элементов, которые хотите добавить в множесто: '))
                for i in range(count_add):
                    first.add(input('Добавьте элемент: '))
                print(*first)
            elif oper == 2:
                count_rem = int(input(('Введите кол-во элементов, чтобы удалить: ')))
                print(*first)
                if count_rem > len(first):
                    print('Невозможно удалить', count_rem, 'элементов, т к', count_rem, '>', len(first))
                else:
                    for i in range(count_rem):
                        in_set = input('Введите элемент, который хотите убрать из множества: ')
                        if in_set in first:
                            first.remove(in_set)
                            print(*first)
                        else:
                            print('Элемент не лежит в множестве')
            oper = int(input(
                'Введите 1, если хотите добавить в множество:  \n ''Введите 2, если хотите удалить элемент из множества: \n'
                'Введите 0, если ничего не хотите менять: \n '))
            print(*first)

    if num == 2:

        oper2 = int(input(
            'Введите 1, если хотите добавить в множество 2:  \n ''введите 2, если хотите удалить элемент из множества 2: \n'
            ' Введите 0, если ничего не хотите менять: \n '))
        while oper2 != 0:
            if oper2 == 1:
                count_add = int(input('Введите кол-во элементов, которые хотите добавить в множесто: '))
                for i in range(count_add):
                    second.add(input('Добавьте элемент: '))
                print(*second)
            elif oper2 == 2:
                count_rem = int(input(('Введите кол-во элементов, чтобы удалить: ')))
                print(*second)
                if count_rem > len(second):
                    print('Невозможно удалить', count_rem, 'элементов, т к', count_rem, '>', len(second))
                else:
                    for i in range(count_rem):
                        in_set = input('Введите элемент, который хотите убрать из множества: ')
                        if in_set in second:
                            second.remove(in_set)
                            print(*second)
                        else:
                            print('Элемент не лежит в множестве')
            oper2 = int(input(
                'Введите 1, если хотите добавить в множество:  \n ''Введите 2, если хотите удалить элемент из множества: \n'
                'Введите 0, если ничего не хотите менять: \n '))
            print(*second)

    start = int(input('Если хотите снова изменить множества, введите 1, иначе 0: '))

print('Множество 1: ', *first)
print('Множество 2: ', *second)

