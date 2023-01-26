import os
def file_extensions():
    file_ext = {}
    print({os.path.splitext(file)[-1] for file in os.listdir(os.getcwd())})


file_extensions()