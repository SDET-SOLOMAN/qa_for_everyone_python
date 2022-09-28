def combine_words(word, **kwargs):
    if kwargs:
        if 'prefix' in kwargs:
            return kwargs['prefix'] + word
        else:
            return word + kwargs['suffix']
    return word


def anagrams(word, words):
    my_list = []
    index = 0

    for num in words:
        print(f"this is my num {num}")

        if len(num) == len(word):
            print(f"len of num and len of word {len(num)}")
            for letter in num:
                print("You are in letter")
                print(letter)
                if letter in word:
                    index += 1
                elif letter not in word:
                    index = 0
                print(index)
        if index == len(num):
            my_list.append(num)
            print(my_list)

    return my_list
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))