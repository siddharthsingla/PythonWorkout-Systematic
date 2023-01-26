import glob
def find_longest_word(filename):
    longest_word = ''
    for line in open(filename):
        if line.strip():

            #print(line)
            temp = max(line.split(), key=len)
            print(temp)
            if len(temp) > len(longest_word):
                longest_word = temp
    return longest_word

def find_all_longest_words(dirname):
    return {filename: find_longest_word(filename) for filename in glob.iglob(f"{dirname}/*")}

print(find_all_longest_words(r"C:\Users\siddh\Documents\Python Scripts"))