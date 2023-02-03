"""Write a function that writes a dict to a CSV file. Each line in the CSV file should
contain three fields: (1) the key, which we’ll assume to be a string, (2) the value,
and (3) the type of the value (e.g., str or int )"""
import csv
def dict_to_csv(dic):
    with open("dict.csv", "w") as fin:
        outfile = csv.writer(fin, delimiter="\t")
        for key, value in dic.items():
            outfile.writerow([key, value, type(value)])

dic = {"a": 1, "b": 2}
dict_to_csv(dic)