def removeDuplicates(s: str) -> str:
    result = ""
    for i in s:
        if result and result[-1] == i:
            result = result[:-1]
        else:
            result = result + i
    print(result)


s = "abbaca"
# Output: "ca"
removeDuplicates(s)
