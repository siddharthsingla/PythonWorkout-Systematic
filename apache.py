def error404(filename):
    for line in open(filename):
        if "404" in line.split():
            print(line[0])