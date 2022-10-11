from random import randint

i = 100
while i > 0:
    a = int(input('Игрок 1 введите количество конфет: '))
    if a > 28 or a < 0:
        raise ValueError('Играй по правилам!!!')
    elif a < 29 and a > 0:
        if i - a == 0:
            print('Победил 1 игрок!')
            break
        elif i - a <= 0:
            raise ValueError('Неверный ход!!!')
        else:
            i = i - a
            print(f'Осталось {i} конфет')
    if i > 28:
        b = randint(1,28)
        i = i - b
        print(f'Игрок 2 забрал {b} конфет')
        print(f'Осталось {i} конфет')
    elif i - b == 0:
        print('Победил 2 игрок!')
        break
    elif i < 28:
        b = randint(1,i)
        print(f'Игрок 2 забрал {b} конфет')
        i = i - b
        print(f'Осталось {i} конфет')
    elif i - b <= 0:
        raise ValueError('Неверный ход!!!')
    else:
        i = i - b
        print(f'Осталось {i} конфет')