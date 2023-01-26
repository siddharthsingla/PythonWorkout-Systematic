import string
def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter.lower() in "aeiou":
            output.append(f"ub{letter}")
        else:
            output.append(letter)
    if word[0] in string.ascii_uppercase:
        output[0] = output[0].capitalize()
    return "".join(output)

print(ubbi_dubbi("Ulk"))