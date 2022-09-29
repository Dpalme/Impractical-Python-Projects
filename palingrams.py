"""Find palindromes and palingrams using a dictionary file."""
import load_dictionary
wrd_lst = load_dictionary.load('2of4brif.txt')


def find_palindromes():
    """Find palindromes (letter palingrams) in a dictionary file."""

    pali_lst = [wrd for wrd in wrd_lst if len(wrd) > 1 and wrd == wrd[::-1]]

    print("\nNumber of Palindromes found: %d" % len(pali_lst))
    print(*pali_lst, sep="\n")


def find_palingrams():
    """Find all word-pair palingrams in a dictionary file."""
    pali_list = []

    words = set(wrd_lst)

    for wrd in words:
        end = len(wrd)
        rev_wrd = wrd[::-1]

        if end > 1:
            for i in range(end):
                if wrd[i:] == rev_wrd[:end-i] and rev_wrd[end-i:] in words:
                    pali_list.append((wrd, rev_wrd[end-i:]))
                if wrd[:i] == rev_wrd[end-i:] and rev_wrd[:end-i] in words:
                    pali_list.append((wrd, rev_wrd[end-i:]))

    print("\nNumber of palingrams: %d" % len(pali_list))
    print(*sorted(pali_list), sep='\n')


find_palingrams()
