# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])
#
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(sum([x for x in list_1 if isinstance(x, int)]))
print(sum(filter(lambda x: isinstance(x, int), list_1)))
print(sum(x for x in list_1 if type(x) == int))
#    - распечатайте все строки, где есть буква 'a'
print(list(filter(lambda x: type(x) == str and 'a' in x, list_1)))
print(list(x for x in list_1 if isinstance(x, str) and 'a' in x))
#
# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
my = ['cat', 'dog', 'horse', 'cow']
print(tuple(my))
print(tuple(map(lambda x: x, my)))


def my_tuple_maker(*args):
    return args


print(my_tuple_maker(*my))
#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# famil_1 = input("fam names").split(", ")
# famil_2 = input("fam names").split(", ")
# print(famil_1)
# print(famil_2)
# if famil_1 > famil_2:
#     print(famil_1)
# elif famil_2 > famil_1:
#     print(famil_2)
# else:
#     print("equal")
# #
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(filter(lambda x: x, my_dictionary.values())))
print(sum(x for x in my_dictionary.values()))
print(sum(my_dictionary.values()))
#
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
#
my_2 = [1, 2, 3, 4, 5, 3, 2, 1]
print(set(my_2))
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
print(set1.difference(set2))