def permutation(r, c=''):
    if len(r) == 0:
        print(c)
    for i in range(0, len(r)):
        newC = c + r[i]
        newR = r[0:i] + r[i + 1:]
        permutation(newR, newC)


l = []
str = "abcd"
print(permutation(str))


# another approach
def permute(s):
    out = []
    # Base case
    if len(s) == 1:
        out = [s]
    else:
        # Iterate over all characters in the string
        for i, c in enumerate(s):
            # For every character, find all possible permutations of the remaining string
            for perm in permute(s[:i] + s[i + 1:]):
                # Add the current character to the permutations of the remaining string
                out += [c + perm]
    return out
