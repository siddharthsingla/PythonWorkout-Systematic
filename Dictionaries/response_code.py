from collections import defaultdict
def response_code(filename):
    IPs = defaultdict(list)
    for line in open(filename):
        fields = line.strip().split()
        ip = fields[0]
        code = fields[8]
        IPs[code].append(ip)
    return IPs


response_code("logfile.txt")