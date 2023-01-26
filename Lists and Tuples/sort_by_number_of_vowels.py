def sort_by_number_of_vowels(strings):
    return (sorted(strings, key=vowel_count))

def vowel_count(string):
    count = 0
    for char in string:
        if char.lower() in "aeiou":
            count += 1
    return count

print(sort_by_number_of_vowels(["teri", "aisi", "di"]))