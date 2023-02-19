a = (4, "e", 6, "i")

print(a[::-1])

# 1
# 2 3
# 4 5 6
n = 1
for i in range(1, 4):
    for j in range(1, i + 1):
        print(n, end=" ")
        n += 1
    print(" ")


s = "I am India"


def count(s):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowelCount = 0
    consonantCount = 0
    for char in set(s):
        if char in vowels:
            vowelCount += 1
        elif char in consonants:
            consonantCount += 1
    print("Vowel Count", vowelCount)
    print("Consonants Count", consonantCount)


count(s.lower())
