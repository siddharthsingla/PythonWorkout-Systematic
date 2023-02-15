def square(x):
    return x**2
def doboth(f1, f2):
    def g(x):
        return f2(f1(x))
    return g

db = doboth(sum, square)



print(db([1,2,3]))