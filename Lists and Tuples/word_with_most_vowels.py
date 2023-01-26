from collections import Counter

def most_repeating_vowel(word):
    d = {}
    for char in word:
        if char.lower() in "aeiou":
            d[char] = d.get(char,0) + 1
    print(d)
    return max(d.values())
def word_with_most_vowels(words):
    return max(words, key=most_repeating_vowel)

print(word_with_most_vowels(["thiiiiis", "is", "eleouamentary"]))