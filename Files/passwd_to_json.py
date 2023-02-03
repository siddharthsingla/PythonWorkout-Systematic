import json
import csv
def passwd_to_json():
    with open("passwd.txt") as infile, open("passwd_json.json", "w") as outfile:
        i = csv.reader(infile, delimiter=":")
        for record in i:
            print(json.dumps(record))
            outfile.write(json.dumps(record))

def passwd_to_jsonv2():
    output = []
    fields = ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8")
    with open("passwd.txt") as infile, open("passwd_json.json", "w") as outfile:
        i = csv.reader(infile, delimiter=":")
        for record in i:
            output.append(dict(zip(fields, record)))
        outfile.write(json.dumps(output))
passwd_to_jsonv2()