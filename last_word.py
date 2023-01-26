def last_word(texfile):
    lastword = chr(0)
    with open(texfile) as f:
        for line in f:
            for word in line.split():
                if word > lastword:
                    lastword = word


    return lastword

print(last_word("sample2.txt"))