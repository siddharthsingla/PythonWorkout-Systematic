def name_triangle():
    name = input("Enter a name: ")
    for i in range(len(name)):
        print(name[:i+1])
name_triangle()