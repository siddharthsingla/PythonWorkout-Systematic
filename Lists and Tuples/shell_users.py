from collections import defaultdict
import operator
def shell_users(filename):
    shells = defaultdict(list)
    for line in open(filename):
        user, *_, shell = line.strip().split(":")
        shells[shell].append(user)
        shells[shell].sort()

    for k, v in sorted(shells.items()):
        print(f"{k}: {v}")

shell_users("passwd.txt")
