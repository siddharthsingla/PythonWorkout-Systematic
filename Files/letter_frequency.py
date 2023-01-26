"""Given a directory, read through each file and count the frequency of each letter.
(Force letters to be lowercase, and ignore nonletter characters.) Use a dict
to keep track of the letter frequencies. What are the five most common letters
across all of these files?"""
from collections import Counter
import glob
import string
def letter_frequency(dirname):
    counts = Counter()
    for file in glob.iglob(f"{dirname}/*"):
        try:
            for line in open(file):
                for char in line:
                    if char in string.ascii_letters:
                        counts.update(char)
        except:
            pass
    return list(dict(counts.most_common(5)).keys())

print(letter_frequency(r"C:\Users\siddh\PycharmProjects\PythonWorkout-Systematic"))