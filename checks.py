def check_for_int(string: str, nat: int = 0) -> bool:
    if len(string) < 1 or (len(string) == 1 and not string.isdecimal()) or string.count('.') > 0:
        return False

    for i in range(0, len(string)):
        char = ord(string[i])

        if 48 <= char <= 57:
            continue
        elif i == 0 and char != 45 and not nat:
            return False
        elif (char < 48 or char > 57) and i > 0:
            return False

    return True


def check_for_float(string: str) -> bool:
    if len(string) < 3 or string.count('.') > 1 or string.count('.') == 0 or string[0] == '.' or string[-1] == '.' or \
            (string[0] == '-' and string[1] == '.'):
        return False

    for i in range(0, len(string)):
        char = ord(string[i])

        if 48 <= char <= 57 or char == 46:
            continue
        elif i == 0 and char != 45:
            return False
        elif (char < 48 or char > 57) and i > 0:
            return False

    return True


def check_for_num(string: str) -> bool:
    if len(string) < 1 or (len(string) == 1 and not string.isdecimal()) or string.count('.') > 1 or\
            string[0] == '.' or string[-1] == '.' or (string[0] == '-' and string[1] == '.'):
        return False

    for i in range(0, len(string)):
        char = ord(string[i])

        if 48 <= char <= 57 or char == 46:
            continue
        elif i == 0 and char != 45:
            return False
        elif (char < 48 or char > 57) and i > 0:
            return False

    return True
