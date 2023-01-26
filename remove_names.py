def remove_names(filename, names):
    for line in open(filename):
        for name in names:
            line.replace(name, len(name)*"_")
        