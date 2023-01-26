def nthword(filename):
    output = []
    for i, line in enumerate(open(filename)):
        if not line.strip():
            continue
        words = line.split()
        if i >= 10:
            break
        if len(words) < i:
            output.append(words[-1])
        else:
            output.append(words[i])
    return " ".join(output)

print(nthword("sample2.txt"))