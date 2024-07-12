import random
import re

print('Выжить или Умереть?!!!')


def r_number():
    random_number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(random_number)
    return n


number = r_number()

print(f'Случайное число: {number}')


def password(n):
    pass_ = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pass_ += str(i) + str(j)
    _pass_ = re.findall(r'\d\d', pass_)
    return _pass_


print('Пароль: ', password(int(number)))
