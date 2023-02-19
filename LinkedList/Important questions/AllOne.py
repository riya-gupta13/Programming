# https://leetcode.com/problems/all-oone-data-structure/
class AllOne:

    def __init__(self):
        self.map = {}

    def inc(self, key: str) -> None:
        if key in self.map.keys():
            self.map[key] += 1
        else:
            self.map.setdefault(key, 1)

    def dec(self, key: str) -> None:
        if key in self.map.keys():
            self.map[key] -= 1
            if self.map[key] == 0:
                del self.map[key]
        else:
            self.map.setdefault(key, 1)

    def getMaxKey(self) -> str:
        if len(self.map) == 0:
            return ""
        else:
            list(sorted(self.map))



