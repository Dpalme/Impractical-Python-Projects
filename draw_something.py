import load_dictionary
from collections import Counter

word_list = sorted(load_dictionary.load('2of4brif.txt'))

lenght = int(input("Lenght: "))
letters = Counter(input("Letters: "))

possible_words = []
for word in word_list:
    if len(word) == lenght:
        possible_words.append(word)


for word in possible_words.copy():
    letters_copy = letters
    for letter in word:
        if letter not in letters:
            if letters_copy[letter] == 0:
                possible_words.remove(word)
                break
        else:
            letters_copy.subtract(letter)

if len(possible_words) >= 1:
    print(possible_words)
    while input("Answer? y/n\n").lower() != 'y':
        letters_copy = letters
        letters = []
        for letter in [x for x in input("Letters: ")]:
            if letter in letters_copy:
                letters.append(letter)
                letters_copy.subtract(letter)
        for word in possible_words.copy():
            for letter in word:
                if letter not in letters:
                    possible_words.remove(word)
                    break
        if len(possible_words) >= 1:
            print("Common Letters: %s" % str(letters))
            print(possible_words)
        else:
            print("Common Letters: %s" % str(letters))
            print("no word in the word list")
else:
    print("no word in the word list")
