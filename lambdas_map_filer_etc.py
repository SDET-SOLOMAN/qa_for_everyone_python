# Map -> TO EVERY ITEM IN THE LIST

print(list(map(lambda x: x*2, [2, 3, 4, 5, 7])))

names = [
    dict(
        first="mike", second='solo'
    ),
    dict(
        first='sam', second='eldante'
    ),
    dict(
        first='sveta', last='davin'
    )
]
print(list(map(lambda x: x['first'], names)))
print(list(map(lambda x: x['first'].capitalize(), names)))

my_list = [1, 2, 3, 4, 5, 6]
s = list(map(lambda x: x-1, my_list))
print(s)


# Filter - filters out per condition

names = ['austin', 'james', 'mike', 'apple']
print(list(filter(lambda x: x[0].lower() == 'a', names)))

instructors = ['james', 'said', 'mark', 'antonio', 'el loko']
print(list(filter(lambda x: len(x) > 5, instructors)))