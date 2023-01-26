def sum_words(filename):
    total = 0
    for line in open(filename):
        total += sum(int(word) for word in line.strip().split() if word.isdigit())
    return total