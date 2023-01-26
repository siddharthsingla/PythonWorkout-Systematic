def different_ips(filename):
    ips = set()
    for line in open(filename):
        ips.add(line.strip().split()[0])
    return ips

def different_ipsv2(filename):
    return {line.strip().split()[0] for line in open(filename)}