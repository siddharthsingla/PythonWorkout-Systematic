def plus_minus(seq):
    print(sum(seq[1::2]) - sum(seq[2::2]) + seq[0])


def plus_minusv2(seq):
    total = seq.pop(0)
    while seq:
        total += seq.pop(0)
        if seq:
            total -= seq.pop(0)
    print(total)

def plus_minusv3(seq):
    total = seq[0]
    for i in range(1, len(seq), 2):
        if i + 1 == len(seq):
            total += seq[i]
            break
        else:
            total = total + seq[i] - seq[i+1]
    print(total)

plus_minusv3([10, 20, 30, 40, 50, 60, 70, 90])