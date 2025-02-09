def validate_phone(num):
    if not validate_input(input):
        return False

    if not num.isdecimal():
        print("not a number")
        return False

    if len(num) < 5 or len(num > 10):
        print("not a phone")
        return False
    return True


def validate_input(input):
    if not input:
        print("Can not be blank")
        return False
    return True
