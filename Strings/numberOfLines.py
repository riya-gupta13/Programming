def numberOfLines(widths: list[int], s: str) -> list[int]:
    # new = ""
    # pixels = 0
    # lines = []
    # pixel = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # for i in range(0, len(s)):
    #     ind = alpha.index(s[i])
    #     pixels += widths[ind]
    #     new += s[i]
    #     if pixels >100:
    #         lines.append(new)
    #         new = ''
    #         pixels = 0
    # print(lines, new, pixels)
    # lines.append(new)
    # print(len(lines))
    # for i in range(0, len(new)):
    #     ind = alpha.index(new[i])
    #     pixel += widths[ind]
    # print(pixel)
    # print([len(lines), pixel])
    lines, width = 1, 0
    for c in s:
        w = widths[ord(c) - ord('a')]
        width += w
        if width > 100:
            lines += 1
            width = w
    print(lines, width)


widths = [7, 5, 4, 7, 10, 7, 9, 4, 8, 9, 6, 5, 4, 2, 3, 10, 9, 9, 3, 7, 5, 2, 9, 4, 8, 9]
s = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
# Output: [3,60]
numberOfLines(widths, s)
