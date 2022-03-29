def is_within_range(num, _min, _max):
    if _min <= num <= _max:
        return True
    return False


def is_even(num):
    return num % 2 == 0


def red_or_blue(num):
    if not is_even(num) or (is_even(num) and is_within_range(num, 6, 20)):
        return 'Red'

    if (is_even(num) and num > 20) or (is_even(num) and is_within_range(num, 2, 4)):
        return 'Blue'