# my_dict = dict(name='james', age=34)
#
# for k,v in enumerate(my_dict.items(),88):
#     print(k,v)

my_ins = dict(name='mike', city='ny', state='florida', color='pink')
print({k.capitalize(): v[0].upper() + v[1:] for k, v in my_ins.items()})

my_list = list(range(0, 99))
print({num: ("Even" if num % 2 == 0 else "Odd") for num in my_list})

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = {list1[i]: list2[i] for i in range(0, 3)}
dict(zip(list1, list2))

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)
