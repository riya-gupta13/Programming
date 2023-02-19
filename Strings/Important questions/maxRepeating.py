def maxRepeating(sequence: str, word: str) -> int:
    ans = 1
    while word * ans in sequence:
        ans += 1
    return ans - 1


sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
maxRepeating(sequence, word)
