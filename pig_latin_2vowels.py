def pig_latin(word):
    if len(set(word.lower()) & set("aeiou")) >= 2:
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"

print(pig_latin("ordi"))