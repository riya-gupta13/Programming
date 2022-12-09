def halvesAreAlike(s: str) -> bool:
    s=s.lower()
    l = len(s) // 2
    count = 0
    counts = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        for j in list(s[:l]):
            if i in j:
                count += 1
        for k in list(s[l:]):
            if i in k:
                counts = counts + 1
    print(count, counts)
    if counts==count:
        print("True")
        return True
    else:
        print("False")
        return False


s = "Uo"
# Output: false
halvesAreAlike(s)
