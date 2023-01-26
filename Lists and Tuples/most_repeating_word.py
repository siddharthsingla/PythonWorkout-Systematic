from collections import Counter

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]
def most_repeating_word(listofwords):
    return max(listofwords, key=most_repeating_letter_count)

print(most_repeating_word(["This", "is", "an", "elemeneetary", "schooool"]))