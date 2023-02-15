def reverse_text(lines):

    return [" ".join(line.split()[::-1]) for line in lines]

print(reverse_text(["abc def", "ghi jkl"]))