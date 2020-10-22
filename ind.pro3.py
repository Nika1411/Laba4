#!/usr/bin/env python3
# -*- config utf-8 -*-

# Вариант 2
# Найти сумму целых положительных чисел, больших 20, меньших 100 и кратных 3

if __name__ == '__main__':
    s = 0
    for i in range(20, 100):
        if i % 3 == 0:
            s += i
    print(s)
