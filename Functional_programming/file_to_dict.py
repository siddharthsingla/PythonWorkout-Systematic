"""Find a configuration file in which the lines look like “name=value.” Use a dict
comprehension to read from the file, turning each line into a key-value pair"""

def file_to_dict(filename):
    return {key: value for line in open(filename) for key, value in line.split("=")}
