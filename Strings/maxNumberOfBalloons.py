import collections


def maxNumberOfBalloons(text: str) -> int:
    d = collections.defaultdict(int)
    s = set("balon")
    for letter in text:
        if letter in s:
            d[letter] += 1

    return min(d['b'], d['a'], d['l'] // 2, d['o'] // 2, d['n'])



text = "loonbalxbllpoon"
# Output: 1
maxNumberOfBalloons(text)
