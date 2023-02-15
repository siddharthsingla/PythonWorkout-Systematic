import string
def letters_in_names(names):
    return {char for name in names for char in name}

def letters_in_namesv2(names):
    return {char for char in ''.join(names) if char in string.ascii_letters}

print(letters_in_namesv2(["teri", "toh", "teri", "taa"]))