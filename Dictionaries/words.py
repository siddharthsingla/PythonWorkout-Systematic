def words(filename):
    output = {}
    for line in open(filename):
        for word in line.strip().split():
            output[word] = output.get(word, 0) + 1
    return output