def unique_response_codes(filename):
    return {line.split()[8] for line in open(filename)}

print(unique_response_codes('apache.txt'))