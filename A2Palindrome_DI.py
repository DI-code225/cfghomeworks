def tellifpalindrome(string):
    count_start = 0
    count_end = len(string) - 1

    while count_end >= count_start:
        if not string[count_start] == string[count_end]:
            return False
        count_start += 1
        count_end -= 1
    return True


string = "reviver"

if tellifpalindrome(string):
    print("The word  " + string + "  is a palindrome")
else:
    print("The word  " + string + "  is not a palindrome")
