"""Create a text file (using an editor, not necessarily Python) containing two tabseparated
columns, with each column containing a number. Then use Python
to read through the file you’ve created. For each line, multiply each first number
by the second, and then sum the results from all the lines. Ignore any line
that doesn’t contain two numeric columns"""

def multiple_columns(filename):
    total = 0
    for line in open(filename):
        fields = line.strip().split()
        if len(fields) != 2:
            continue
        if not (fields[0].isdigit() and fields[1].isdigit()):
            continue
        total += int(fields[0]) * int(fields[1])
    return total