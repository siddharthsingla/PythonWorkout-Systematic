import string
def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    def password_check(password):
        uc = lc = punc = digits = 0
        for char in password:
            if char in string.ascii_lowercase:
                lc += 1
            elif char in string.ascii_uppercase:
                uc += 1
            elif char in (",.!"):
                punc += 1
            elif char in string.digits:
                digits += 1
        if uc < min_uppercase or lc < min_lowercase or punc < min_punctuation or digits < min_digits:
            return False
        else:
            return True

    return password_check

def create_password_checkerv2(min_uppercase, min_lowercase, min_punctuation, min_digits):
    uc = set(string.ascii_uppercase)
    lc = set(string.ascii_lowercase)
    punc = set(string.punctuation)
    digits = set(string.digits)
    def password_checkv2(string):
        if len([char for char in string if char in uc]) < min_uppercase:
            return False
        if len([char for char in string if char in lc]) < min_lowercase:
            return False
        if len([char for char in string if char in digits]) < min_digits:
            return False
        if len([char for char in string if char in punc]) < min_punctuation:
            return False
        else:
            return True
    return password_checkv2

x = create_password_checkerv2(1, 5, 1, 2)
if x("passworD123!"):
    print("good")