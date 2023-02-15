import string
def gematria():
     return {char: index for index, char in enumerate(string.ascii_letters, 1)}

GEMATRIA = gematria()
def gematria_for(word):
    return sum(GEMATRIA.get(char, 0) for char in word)

def gematria_equal_words(input_word):
    input_word_score = gematria_for(input_word)
    return [word.strip() for word in open('/usr/share/dict/words') if gematria_for(word.strip()) == input_word_score]

print(gematria_equal_words("zebra"))