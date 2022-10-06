# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001 - π = 3.141, 10^{-1} ≤ d ≤10^{-10}

import math as m
import util as u

num1 = 0.00001
num2 = 0.001
precision1 = u.getFractionalSymbolsAmount(num1)
precision2 = u.getFractionalSymbolsAmount(num2)
print(f'Число Пи с точностью по умолчанию: {m.pi}')
print(f'Число Пи с точностью {u.getStrNoExp(num1)}: {round(m.pi, precision1)}')
print(f'Число Пи с точностью {u.getStrNoExp(num2)}: {round(m.pi, precision2)}')
