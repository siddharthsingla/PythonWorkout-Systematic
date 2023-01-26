def pig_latin(word):
    x = ""
    if word[-1] in ".,!":
        x = word[-1]
        word = word[:-1]
        print(word)

    if word[0].lower() in "aeiou":
        output = f"{word}way"
    else:
        output = f"{word[1:]}{word[0]}ay"
    return f"{output}{x}"

print(pig_latin("ord."))