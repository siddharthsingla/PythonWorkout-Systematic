def word_lengths(filename):
    return {len(word) for line in open(filename) for word in line.split()}

