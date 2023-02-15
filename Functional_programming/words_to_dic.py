def words_to_dic(words):
    return {word: vowel_count(word) for word in words.split()}

def vowel_count(word):
    return len([char for char in word if char.lower() in "aeiou"])

print(words_to_dic("this is an easy test"))