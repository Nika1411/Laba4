#!/usr/bin/env python3
# -*- config utf-8 -*-
# U=max^2(x^2y,xy^2)+min^2(x-y,x+2y)

# Вариант 2
#  Даны действительные числа x и y . Найти U=max^2(x^2y,xy^2)+min^2(x-y,x+2y). Для
# минимума и максимума использовать условный оператор if .

if __name__ == '__main__':
    x = int(input("Введите X: "))
    y = int(input("Введите Y: "))
    if x * x * y < x * (y * y):
        maxim = x * (y * y)
    else:
        maxim = x * x * y
    if x - y > x + 2 * y:
        minim = x + 2 * y
    else:
        minim = x - y
    U = maxim ** 2 + minim ** 2
    print(U)



