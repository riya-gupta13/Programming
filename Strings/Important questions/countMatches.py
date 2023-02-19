def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    count = 0
    for i in items:
        if ruleKey == "type":
            if ruleValue == i[0]:
                print("Matchedone", i)
                count = count + 1
        if ruleKey == "color":
            if ruleValue == i[1]:
                print("Matchedtwo", i)
                count = count + 1
        if ruleKey == "name":
            if ruleValue == i[2]:
                print("Matchedthree", i)
                count = count + 1
    print(count)


items = [["ii", "iiiiiii", "ii"], ["iiiiiii", "iiiiiii", "ii"], ["ii", "iiiiiii", "iiiiiii"]]
ruleKey = "color"
ruleValue = "ii"
# Output: 0
countMatches(items, ruleKey, ruleValue)
