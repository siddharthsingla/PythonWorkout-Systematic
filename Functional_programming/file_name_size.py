import os
import glob
def file_name_size(dir):
    return {file: os.stat(file).st_size for file in glob.glob(f"{dir}/*") if os.path.isfile(file)}
