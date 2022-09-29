"""A function that given a string prints a bar chart with the frecuency of
each letter"""


def main(text):
    """A function that given a string prints a bar chart with the frecuency of
    each letter to the terminal

    Args:
      - text: The text to be analyzed.
    """

    letterCount = {chr(number): 0 for number in range(ord("a"), ord("z") + 1)}

    for letter in text.lower():
        if letter.isalpha():
            letterCount[letter] += 1

    print(letterCount)

    for key, value in letterCount.items():
        print("%s : " % key + ("[%s]" % key) * value)


if __name__ == "__main__":
    main(input("Text to be analyzed:\n"))
