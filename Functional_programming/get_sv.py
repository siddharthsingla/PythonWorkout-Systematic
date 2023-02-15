def get_sv(filename):
    return {word for word in open(filename) if len(set(word) & set("aeiou")) >= 5}