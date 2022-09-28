# Scope of variables
import math as m

x = 100  # <- Global Scope


def my_func():
    x = 500  # <- Local Scope
    print(x)


print(my_func())

# ---------------

x, y = 15, 78


def sum_it(x, y):
    print(f"Locals: {locals()}")
    return x, y


print(f"Inside the function of sum_it: {sum_it(5, 8)}")
print(f"Outside the function: {x + y}")
print(f"Globals: {globals()}")

# ----------------
# Lambda

print((lambda x, y: x * y)(5, 8))

multipl = lambda x, y: x * y
print(multipl(5, 5))

# filtering with Lambda
my_list = ['name', 1, 4, None, {982: "Name"}, 322.1, "vasya", 'pizza', 9]


# instead of Looping to find int or float in the list and sum those up:

def my_filter_and_sum(my_l):
    updated_l = []
    for num in my_l:
        if type(num) == int or type(num) == float:
            updated_l.append(num)
    return sum(updated_l)


# or

def my_filter_and_sum2(my_l):
    updated_l = []
    for num in my_l:
        if isinstance(num, int) or isinstance(num, float):
            updated_l.append(num)
    return sum(updated_l)


print(my_filter_and_sum(my_list))
print(my_filter_and_sum2(my_list))

# VS. LAMBDA:

print(sum(filter(lambda x: isinstance(x, int) or isinstance(x, float), my_list)))


# ----------------

# Filter odd nums:

def odd_num_filter(num):
    if isinstance(num, int) and num % 2 != 0:
        return True
    return False


# using lambda:
print(list(filter(lambda num: isinstance(num, int) and num % 2 != 0, my_list)))

# ----------

# finding which str in list got letter A in them

my_list = ['name', 1, 4, None, {982: "Name"}, 322.1, "vasya", 'pizza', 9, "no_n", "emil", "petro", 'samsa']


def find_a(my_l):
    my_local_list = []
    for num in my_l:
        if type(num) == str and 'a' in num.lower():
            my_local_list.append(num)
    return my_local_list


print(find_a(my_list))

# using Lambda:
print(list(filter(lambda num: isinstance(num, str) and 'a' in num.lower(), my_list)))

# or List Comprehension
print([x for x in my_list if type(x) == str and 'a' in x.lower()])

# ---------------

from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8]))

from my_file import *

res = sum_it(5, 10)
res1 = prod(11, 12)


def testing():
    assert sum_it(5, 8) == 13, f"Wrong numbers"
    assert div(10, 0) == 0, f"Can't divide by Zero"


print(testing())

# ----------

my_list = [x for x in range(1, 99)]
print(m.prod(my_list))

# ----------

import datetime as dt
birth_year = 1989
current_date = dt.date.today()
current_age = current_date.year - birth_year
current_month = current_date.month
print(current_date)
print(current_age)
print(current_month)