def funcfile(filename, fn):
    ' '.join(fn(word) for line in open(filename) for word in line.split())

def fn(word):
    pass