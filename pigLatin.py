"""A simple function that translates a word to Pig Latin"""


def main(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        return "-".join((word, "way"))
    else:
        return "-".join((word[1:], word[0], "ay"))


if __name__ == "__main__":
    input_text = input("Text to be translated: ")
    if ' ' not in input_text:
        print(main(input_text))
    else:
        output = ''
        for word in input_text.split():
            output = " ".join([output, main(word)])
        print(output)
