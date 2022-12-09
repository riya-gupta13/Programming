def sortByBits(arr: list[int]) -> list[int]:
    return sorted(sorted(arr), key=lambda x: bin(x).count('1'))