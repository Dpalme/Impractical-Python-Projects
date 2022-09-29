import random
from secrets import choice
from functools import lru_cache
from collections import Counter


@lru_cache(None)
def load_words() -> set:
    with open('2of4brif.txt') as in_file:
        return {
            w.lower()
            for w in in_file.read().rsplit("\n")
            if len(w) == 5
        }


def main():
    def play_round(word, guess):
        return ''.join(
            '-' if l not in word else (
                '#' if word[i] == l else '*')
            for i, l in enumerate(guess))
        
    def random_word() -> str:
        return choice(tuple(load_words()))

    def ai_play():
        word = random_word()
        words = load_words()
        while True:
            guess = words.pop()
            res = play_round(word, guess)
            if res == '#' * len(guess):
                return True
            for i, [r, l] in enumerate(zip(res, guess)):
                if r == '-':
                    words = {w for w in words if l not in w}
                elif r == '*':
                    words = {w for w in words if l in w}
                else:
                    words = {w for w in words if l == w[i]}
            if len(words) == 0:
                return False
    
    def ai_solve():
        words = load_words()
        while True:
            guess = words.pop()
            res = input(f'{guess}\n> ')
            if res == '#' * len(guess):
                return True
            for i, [r, l] in enumerate(zip(res, guess)):
                if r == '-':
                    words = {w for w in words if l not in w}
                elif r == '*':
                    words = {w for w in words if l in w}
                else:
                    words = {w for w in words if l == w[i]}
            if len(words) == 0:
                return False
    
    def statistics():
        words = load_words()
        print('overall', *Counter((l for w in words for l in w)).most_common(5))
        print('p/pos', *(Counter(s).most_common(1)[0]for s in zip(*words)))

    ai_solve()



if __name__ == '__main__':
    main()
