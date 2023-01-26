def longest_word(texfile):
    longest = ""
    with open(texfile) as f:
        for line in f:
            for word in line.split():
                if len(word) > len(longest):
                    longest = word


    return longest

print(longest_word("sample2.txt"))