name = 'mike sdet'
print([x[0].upper() for x in name])

print([x * 3 for x in range(0, 83)])

print([str(x) for x in range(0, 837)])

print([x for x in range(1, 76) if x % 2 == 0])
print([f"This x: {x} is even" if x % 2 == 0 else f"{x} is not even" for x in range(1, 76)])

name = "JAmeEs EL Ausioe Del Toro"
print(''.join([x for x in name if x.lower() not in 'aeiou']))

answer = [x[0] for x in ["Elie", "Tim", "Matt"]]

answer2 = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]


# nested / multid dimensional list

my_n_l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([[x for x in l if x % 2 == 0 ] for l in my_n_l])

print([["X" if x % 2 == 0 else "O" for x in range(2, 5)] for l in range(0, 3) ])