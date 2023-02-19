def maximumValue(strs: list[str]) -> int:
    ans = []
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    digits = "1234567890"
    for i in strs:
        new = sorted(i)
        if new[-1] in digits:
            ans.append(int(i))
        else:
            ans.append(len(i))
    print(ans)
    print(max(ans))

    #     print(sorted(i))
    #     for j in i:
    #         if j in alphabets and i[1:] in digits:
    #             print("i", i)
    #             ans.append(len(i))
    #             break
    #         elif j in alphabets:
    #             print("i", i)
    #             ans.append(len(i))
    #             break
    #         else:
    #             print(i)
    #             ans.append(int(i))
    #             break
    # print(ans)
    # print(max(ans))


strs = ["iw1", "61939", "7", "7i", "cye", "bv7yg", "t3ye6", "990"]
maximumValue(strs)
