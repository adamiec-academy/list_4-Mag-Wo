def is_palindrome(text):
    x = text.lower()
    y = x.split()
    z = "".join(y)

    if z == z[::-1]:
        return True
    else:
        return False

   
