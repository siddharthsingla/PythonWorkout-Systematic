def anyjoin(args, glue=" "):
    output = f"{args[0]}"
    for arg in args[1:]:
        output += f"{glue}{arg}"
    return output

print(anyjoin([1,2,3]))
print(anyjoin('abc','**'))