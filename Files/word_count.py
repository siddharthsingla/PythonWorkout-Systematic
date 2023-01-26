def word_count(filename):
    no_of_chars = 0
    no_of_words = 0
    no_of_lines = 0
    unique_words = set()

    for line in open(filename):
        for char in line:
            no_of_chars += 1
        no_of_lines += 1
        no_of_words += len(line.strip().split())
        unique_words.update(set(line.strip().split()))
    print(no_of_chars, no_of_words, no_of_lines, len(unique_words))

word_count("wcfile.tx")