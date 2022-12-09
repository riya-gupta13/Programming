def isPalindrome(s: str) -> bool:
    string = ""
    for i in s:
        if i.isalnum():
            string += i
    string = string.lower()
    print(string)
    rev = string[::-1]
    if string == rev:
        return True
    return False


s = "0P"
print(isPalindrome(s))
