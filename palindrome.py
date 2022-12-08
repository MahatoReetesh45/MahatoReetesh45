def check_Palindrome(value):
    rev = value[::-1]
    if( rev == value):
        return True
    else:
        return False
print(check_Palindrome('data'))