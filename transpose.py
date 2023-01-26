def transpose(words):
    output = []
    for i in range(len(min(word.split() for word in words))):
        temp = []
        for word in words:

            temp.append(word.split()[i])
        output.append(" ".join(temp))
    return output


def transposev2(words):
    return [" ".join(t) for t in (zip(*[word.split() for word in words]))]
print(transposev2(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))