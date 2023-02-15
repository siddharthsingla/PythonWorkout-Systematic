import os
import glob

def file_stats(dirname):
    return {file: os.stat(os.path.join(dirname, file)).st_size for file in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, file))}

print(file_stats("/etc"))