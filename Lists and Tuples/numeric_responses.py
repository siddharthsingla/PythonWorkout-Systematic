def numeric_responses(filename):
    output = {}
    for line in open(filename):
        code = line.split()[8]
        output[code] = output.get(code, 0) + 1
    print(output)

numeric_responses("mini-access-log.txt")