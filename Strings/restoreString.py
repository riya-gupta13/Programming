def restoreString(s: str, indices: list[int]) -> str:
    str = list(s)
    for i in range(0, len(indices)):
        str[indices[i]] = s[i]
    print("".join(str))


s = "abc"
indices = [0, 1, 2]
restoreString(s, indices)
# s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
