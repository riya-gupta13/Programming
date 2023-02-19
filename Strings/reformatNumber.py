def reformatnumber(number: str) -> str:
    if '-' in number:
        number = number.replace('-', '')
    if ' ' in number:
        number = number.replace(' ', '')
    print(number)
    res = []
    while len(number) != 0:
        if len(number) > 4:
            frst = number[:3]
            res.append(frst)
            number = number.removeprefix(number[:3])
            print(frst, number)
        if len(number) == 3:
            second = number[:3]
            res.append(second)
            number = number.removeprefix(number[:3])
            print(second, number)
        if len(number) == 2 or len(number) == 4:
            third = number[:2]
            res.append(third)
            number = number.removeprefix(number[:2])
            print(third, number)
    print("-".join(res))


number = "12"
# Output: "123-456"
reformatnumber(number)
