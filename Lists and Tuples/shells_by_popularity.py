def shells_by_popularity(filename):
    shells = {}
    for line in open(filename):
        shell = line.strip().split(":")[-1]
        shells[shell] = shells.get(shell, 0) + 1
    for shell in sorted(shells.items(), key=lambda item: item[1], reverse=True):
        print(shell)

import operator
from collections import Counter
def shells_by_popularityv2(filename):
    shells = Counter(line.strip().split(":")[-1] for line in open(filename) if not line.startswith(("#", "\n")))
    return sorted(shells.items(), key=operator.itemgetter(1), reverse=True)

print(shells_by_popularityv2("passwd.txt"))