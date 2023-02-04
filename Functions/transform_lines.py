def transform_lines(fn, infile, outfile):
    with open(outfile, "w") as out:
        for line in open(infile):
            out.write(fn(line))

