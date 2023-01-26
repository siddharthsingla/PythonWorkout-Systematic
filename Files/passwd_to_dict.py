
def passwd_to_dict(filename):
    passwd = {}
    for line in open(filename):
        if not line.startswith(("#", '\n')):
            fields = line.split(":")
            passwd[fields[0]] = int(fields[2])
    return passwd