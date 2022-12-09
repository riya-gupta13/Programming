import re


def freqAlphabets(s: str) -> str:
    dic = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j',
           '11': 'k', '12': 'l', '13': 'm',
           '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w',
           '24': 'x', '25': 'y',
           '26': 'z'}
    pointer = 0
    res = ''
    while pointer < len(s) - 2:
        if s[pointer + 2] == '#':
            res += dic[s[pointer:pointer + 2]]
            pointer += 3
        else:
            res += dic[s[pointer]]
            pointer += 1
    if pointer == len(s) - 2:
        res += dic[s[-2]]
        res += dic[s[-1]]
    elif pointer == len(s) - 1:
        res += dic[s[-1]]
    return res

    # pattern = '\d{0,2}#'
    # res = re.findall(pattern, s)
    # l = []
    # n = ''
    # print(res)
    # st = "".join(res)
    # if s.__contains__(st):
    #     n = s.replace(st, '')
    # n=list(n)
    # print(n)
    # for i in res:
    #     new = re.sub('#', '', i)
    #     l.append(new)
    # print(l)
    # n.extend(l)
    # for i in range(0, len(n)):
    #     n[i] = alpha[int(n[i])]
    # print("".join(n))


s = "10#11#12"

# Output: "jkab"
freqAlphabets(s)
