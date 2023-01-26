def ascii_encode(sentence):
    output = []
    for char in sentence:
        if not char.isalnum():
            output.append(hex(ord(char)).replace('0x', '%'))
        else:
            output.append(char)
    return "".join(output)

print(ascii_encode("hello world!"))