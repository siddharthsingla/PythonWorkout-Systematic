"""Extend this exercise by asking the user to enter a space-separated list of inte-
gers, indicating which fields should be written to the output CSV file. Also ask
the user which character should be used as a delimiter in the output file. Then
read from /etc/passwd , writing the user’s chosen fields, separated by the user’s
chosen delimiter."""

import csv
def passwd_to_csv():
    fields = input("enter column numbers: ").strip()
    fields = fields.split()
    with open("../Lists and Tuples/passwd.txt") as fin, open("passwd.csv", "w") as fout:
        i = csv.reader(fin, delimiter=":")
        o = csv.writer(fout, delimiter="\t")
        for row in i:
            if len(row) > 1:
                o.writerow([row[int(x)] for x in fields])

passwd_to_csv()