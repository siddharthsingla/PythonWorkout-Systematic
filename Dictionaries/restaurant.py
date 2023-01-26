MENU = {}
def restaurant():
    output = 0
    while True:
        x = input("Enter a food item: ").strip()
        if not x:
            break
        if x not in MENU:
            print(f"{x} is Not on the menu")
        output += MENU[x]
    return output

