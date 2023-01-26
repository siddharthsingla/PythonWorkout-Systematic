"""Create a dict in which the keys are the names of files on your system and the values
are the sizes of those files. To calculate the size, you can use os.stat
(http://mng.bz/dyyo)."""
import os
import glob
def filesize(dirname):
    output = {}
    for file in os.listdir(dirname):
        file = os.path.join(dirname, file)
        if os.path.isfile(file):
            output[file] = os.stat(os.path.join(dirname, file)).st_size

    print(output)

def filesizev2(dirname):
    output = {}
    for file in glob.iglob(f"{dirname}/**/*", recursive=True):
        if os.path.isfile(file):
            output[file] = os.stat(file).st_size

    print(output)
filesizev2(r"C:\Users\siddh\PycharmProjects\PythonWorkout-Systematic")