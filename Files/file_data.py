import json
import os
import glob
import json
def file_stats(dirname):
    output = []
    print(dirname)
    for file in glob.glob(f"{dirname}/*"):
        print(file)
        if os.path.isfile(file):
            file_stats = {}
            file_stats["name"] = file
            file_stats["size"] = os.stat(file).st_size
            file_stats["mtime"] = os.stat(file).st_mtime
            output.append(file_stats)
    print(output)
    w = open("file_stats.json", "w")
    w.write(json.dumps(output))

file_stats(r"/home/sid/PycharmProjects/pythonworkout")