def copyfile(srcfile, *args):
    for arg in args:
        with open(srcfile) as infile, open(arg, "w") as outfile:
            for line in infile:
                outfile.write(line)

copyfile("passwd.txt", "copy1.txt", "copy2.txt")