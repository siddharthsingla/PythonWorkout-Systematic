"""Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation."""
from collections import defaultdict
def vowel_count(filename):
    count = defaultdict(int)
    for line in open(filename):
        for char in line:
            if char.lower() in "aeiou":
                count[char] = count[char] + 1
    return count

def vowel_countv2(filename):
    count = dict.fromkeys("aeiou", 0)
    for line in open(filename):
        for char in line:
            if char.lower() in "aeiou":
                count[char] = count[char] + 1
    return count

vowel_countv2("passwd.txt")
