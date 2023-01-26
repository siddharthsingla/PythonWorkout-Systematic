def sort_names(names):
    return ', '.join(name for name in sorted(names.split()))

print(sort_names("Tom Dick Harry"))