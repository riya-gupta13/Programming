def addBinary(a: str, b: str) -> str:
    sum = int(a, 2) + int(b, 2)
    print(bin(sum)[2:])


a = "1010"
b = "1011"
# Output: "100"
addBinary(a, b)
