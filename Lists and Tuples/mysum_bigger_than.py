def mysum_bigger_than(minimum, *args):
    total = 0
    for arg in args:
        if arg > minimum:
            total += arg
    print(total)

mysum_bigger_than(10, 5, 6, 20, 30)