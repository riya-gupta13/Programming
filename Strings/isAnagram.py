def isAnagram(s: str, t: str) -> bool:
    if sorted(s) == sorted(t):
        return True
    return False

s = "rat"
t = "car"
# Output: true
print(isAnagram(s,t))