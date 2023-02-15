def hex_sum(stringofhex):
    return sum(int(num, 16) for num in stringofhex.split())