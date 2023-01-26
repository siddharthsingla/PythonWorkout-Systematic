import arrow
import os
def file_details():
    output = {}
    dirname = r"C:\Users\siddh\Documents\Python Scripts"
    for file in os.listdir(dirname):
        file = os.path.join(dirname, file)
        if os.path.isfile(file):
            print(file, os.stat(file).st_mtime)

file_details()