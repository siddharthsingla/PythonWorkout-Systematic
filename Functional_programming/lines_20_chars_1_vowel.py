import string
def lines_with_vowels_and_chars(filename):
    return [line for line in open(filename) if len(line) > 20 and contains_vowel(line)]

def contains_vowel(line):
    for char in line:
        if char in string.ascii_letters:
            if char.lower() in "aeiou":
                return True
            return False

def lines_with_vowels_and_charsv2(filename):
    return [line for line in open(filename) if len(filename > 20 and len(set("aeiou") & set(line)) >= 1)]