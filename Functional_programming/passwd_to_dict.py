def passwd_to_dict():
    return {fields[0]: fields[2] for line in open('/etc/passwd') for fields in line.split(":")}