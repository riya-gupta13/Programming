def groupAnagrams(strs: list[str]) -> list[list[str]]:
    strs_table = {}

    for string in strs:
        sorted_string = ''.join(sorted(string))

        if sorted_string not in strs_table:
            strs_table[sorted_string] = []

        strs_table[sorted_string].append(string)

    return list(strs_table.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)
