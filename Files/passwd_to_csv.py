import csv
def passwd_to_csv(filename):
    with open("passwd.csv", "w") as fout, open(filename) as fin:
        infile = csv.reader(fin, delimiter=":")
        outfile = csv.writer(fout, delimiter="\t")
        for record in infile:
            if len(record) > 1:
                outfile.writerow([record[0], record[2]])

passwd_to_csv("../Lists and Tuples/passwd.txt")