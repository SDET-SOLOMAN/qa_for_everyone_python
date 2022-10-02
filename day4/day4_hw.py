# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
from functools import reduce


def square_(x):
    return 4 * x, x * x, x * 2 ** 0.5


#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
my_dict = dict(name="James", job='QA', age=35, ptown="Phindeliea")


def my_lib(**kwargs):
    return kwargs.items()


print(my_lib(**my_dict))

#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

my_list = [20, -3, 15, 2, -1, -21]

print(list(filter(lambda x: x > 0, my_list)))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
#
my_adding = lambda x, y: x + y
my_substract = lambda x, y: x - y
my_multi = lambda x, y: x * y
my_divide = reduce(lambda x, y: x / y, my_list)


print(reduce(my_adding, my_list))
print(my_divide)

from my_calc import  *

signs = "/"
if signs in ["+", "/"]:
    print(sign(45, 0, signs))
else:
    print("Wrong sign")