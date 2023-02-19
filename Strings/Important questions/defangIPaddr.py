def defangIPaddr(address: str) -> str:
    target = {39: None}
    # where 39, 91, and 93 are the ASCII codes for “,” , “[“ and “]” respectively.
    address = "1.1.1.1".replace('.', str(['.'])).translate(target)
    print(str(address))
    address = address.replace('.','[.]')
    print(address)


address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
defangIPaddr(address)
