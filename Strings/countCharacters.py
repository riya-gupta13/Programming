import collections


def countCharacters(words: list[str], chars: str) -> int:
    # d = dict()
    # for i in chars:
    #     d[i] = chars.count(i)
    # print(d)
    # sum = 0
    # for w in words:
    #     d2=collections.Counter(w)
    #     if all(d[j]>=d2[j] for j in d2):
    #         sum+=len(w)
    # print(sum)
    dct1 = collections.Counter(chars)
    res = 0
    for word in words:
        dct2 = collections.Counter(word)
        if all(dct1[el] >= dct2[el] for el in dct2):
            res += len(word)
    print(res)


words = ["cat","bt","hat","tree"]
chars = "atach"
#
# words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
#          "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl", "boygirdlggnh",
#          "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
#          "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
#          "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
#          "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr", "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
#          "oxgaskztzroxuntiwlfyufddl", "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
#          "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv", "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
#          "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
#          "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
#          "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob",
#          "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs", "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]
# chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
# Output: 6
countCharacters(words, chars)
