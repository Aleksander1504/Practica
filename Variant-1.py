
DEBUG = True


def trace(func):
    if not DEBUG:
        return func

    def wrapper(*args):
        print(f"Функция: '{func.__name__}' начиная с параметра: {args}")
        res = func(args)
        print(f"Время: {time.time()-start}")
        print(f"Result: {res}")
        return res
    return wrapper
#Не могу проверить, так как в PyCharm ошибка "Error: Python interpreter is not selected. Please setup Python interpreter first."

SQFT_PER_ACRE = 0
length = int(input("Ввелите длину участка в футах: "))
width = int(input("Ввелите ширину участка в футах: "))

@trace
def func1(*args):
        SQFT_PER_ACRE = (length * width) * 0.000023
        print(f'Участок длиной в {length} футов и шириной {width} футов имеет площадь {SQFT_PER_ACRE} акров')


import math
d = int(input("Назовите высоту в метрах, с которой объект будет отпущен: "))
a = 9.81
Vi = 0

@trace
def func2(*args):
    print("Cкорость при соприкосновении объекта с землей: ",math.sqrt(Vi ** 2 + 2 * a * d))
