def truncateSentence(s: str, k: int) -> str:
    l = s.split()
    print(l[:k])
    print(" ".join(l[:k]))


s = "Hello how are you Contestant"
k = 4
# Output: "Hello how are you"
truncateSentence(s, k)
