"""Find anagrams for single words or phrases using a dictionary file."""
import load_dictionary
from collections import Counter

word_list = load_dictionary.load('2of4brif.txt')
word_list.append("i")
word_list.append("a")
word_list = sorted(word_list)


def singleWordAnagram(word):
    """Find palindromes (letter palingrams) in a dictionary file.

    Args:
      - word: the word to find anagrams for.

    Returns:
      - List of anagrams found."""

    sorted_word = sorted(word)

    anagrams = []

    for current_word in word_list:
        if sorted_word == sorted(current_word) and word != current_word:
            anagrams.append(current_word)

    return anagrams


def phraseAnagrams(name):
    """Build a phrase anagram given a name in a dictionary file.

    Args:
      - word: the word to find anagrams for.

    Returns:
      - Final phrase.
    """
    letter_count = Counter(name)
    limit = len(name.strip(" "))
    anagram = ""

    while len(anagram.strip(" ")) < limit:
        fits = []
        for word in word_list:
            counted_word = Counter(word)
            for k in counted_word:
                if counted_word[k] > letter_count[k]:
                    break
            else:
                fits.append(word)
        if fits != []:
            print("Possible words: " + str(fits))
            print("\nRemaining letters: " + str(counted_word))
            print("\nCurrent phrase: %s" % anagram)
            new_word = input("Word to try to input: ").lower()
            counted_new_word = Counter(new_word)
            for k in counted_new_word:
                if counted_new_word[k] > letter_count[k]:
                    print("\nWord isn't a possible match\n")
                    break
            else:
                anagram = " ".join((anagram, new_word))
                letter_count.subtract(new_word)
        else:
            print("No possible fits remaining")
            break

    print("\nFinal anagarm: %s" % anagram)

    if input("Start over? Y/N\n").lower() == "y":
        if input("Retry with the same word? Y/N\n").lower() == "y":
            phraseAnagrams(name)
        else:
            phraseAnagrams(input("Phrase to find anagram for: "))


phraseAnagrams(input("Phrase to find anagram for: "))
