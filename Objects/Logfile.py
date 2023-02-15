class Logfile():
    def __init__(self, filename):
        self.file = open(filename, "w")

lf = Logfile("test_file.txt")
lf.file.write("this is a tst")