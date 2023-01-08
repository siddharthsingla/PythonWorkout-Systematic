def sum_objects(listofobjects):
    total = 0
    for obj in listofobjects:
        try:
            num = int(obj)
            print(num)
            total += num
        except Exception:
            pass

    return total

def is_intable(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    except TypeError:
        return False
def sum_objectsv2(listofojects):
    return sum(int(num) for num in listofojects if is_intable(num))

print(sum_objectsv2([1, 2, "10", "c", None, 3]))