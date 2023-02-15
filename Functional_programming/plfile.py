def plfile(filename):
    ' '.join(plword(word) for line in open(filename) for word in line.split())

def plword(word):
    if word[0] in "aeiou":
        return word + 'way'
    return word[1:] + word[0] + 'ay'
