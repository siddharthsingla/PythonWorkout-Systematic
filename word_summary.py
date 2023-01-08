def word_summary(words):
    shortest = len(words[0])
    longest = len(words[0])
    total = len(words[0])
    for word in words[1:]:
        if len(word) < shortest:
            shortest = len(word)
        if len(word) > longest:
            longest = len(word)
        total += len(word)
    return (shortest, longest, total/len(words))

def word_summaryv2(words):
    return (min(words, key=len), max(words, key=len), sum(len(word) for word in words)/len(words))

def word_summaryv3(words):
    word_lengths = [len(word) for word in words]
    return (min(word_lengths), max(word_lengths), sum(x for x in word_lengths)/len(word_lengths))

print(word_summaryv3(["teri", "lani", "pani", "ae", "kuttiye", "ni", "kuttiye"]))