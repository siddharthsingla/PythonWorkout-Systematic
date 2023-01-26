"""Ask the user to enter the name of a text file and then (on one line, separated by
spaces) words whose frequencies should be counted in that file. Count how
many times those words appear in a dict, using the user-entered words as the
keys and the counts as the values."""

from collections import defaultdict
def word_frequency():
    output = defaultdict(int)
    file_words = input("Enter filename and words: ")
    filename, *words = file_words.strip().split()
    for line in open(filename):
        for word in words:
            if word in line:
                output[word] = output[word] + 1
    print(output)

word_frequency()