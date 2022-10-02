# # def scramble(s1, s2):
# #     s2 = [x for x in s2]
# #     print(s2)
# #     l = []
# #     for n in s1:
# #         print(f"this is {n}")
# #         print(f"This is l count {l.count(n)}")
# #         print(f'This is s count {s2.count(n)}')
# #         if n in s2 and l.count(n) < s2.count(n):
# #             print(f"inside of if {n}")
# #             l.append(n)
# #     print(l)
# #     if len(l) == len(s2):
# #         return True
# #     return False
# # print(scramble('cedewaraaossoqqyt', 'codewars',))
#
# def multiplicationTable(size):
#     return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]
# print(multiplicationTable(3))
#
#
# import string
# def high(x):
#     x = x.split(" ")
#     print(x)
#     alphabet = list(string.ascii_lowercase)
#     my_dict = {alphabet[i] : i + 1 for i in range(0, len(alphabet))}
#     print(my_dict)
#     score = 0
#     score2 = 0
#     word = ''
#     for n in x:
#         print(word)
#         for s in n:
#             score2 += my_dict[s]
#             print(score2)
#         if score2 > score:
#             word = n
#             score = score2
#         score2 = 0
#     return word
# print(high('man i need a taxi up to ubud'))
# my_list = [[1, 2, 3, 4], [8, 9, 0, 32, 1], [5, 4, 3, 2]]
# print('\n'.join(','.join(str(x) for x in num) for num in my_list))
# print('\n'.join(','.join(map(str, line)) for line in my_list))

list1 = [1, 2, 3, 4]
list2 = [2, 4, 5, 2, 1, 2]

from functools import *

def sum_arr(*args):
    return sum(args)

def sum_2(*args):
    return sum(map(lambda args1: args1, args))

def sum_3(*args):
    return reduce(lambda x, y: x + y, args)

print(sum_arr(*list1, *list2))
print(sum_2(*list1, *list2))
print(sum_3(*list1, *list2))