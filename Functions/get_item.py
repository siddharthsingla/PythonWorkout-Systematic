def get_item(arg):
    def return_item(x):
        return arg[x]
    return return_item

d = {'a':1, 'b':2}
f = get_item(d)
g = get_item([1,2,3,4,5])
print(f("a"))
print(g(4))