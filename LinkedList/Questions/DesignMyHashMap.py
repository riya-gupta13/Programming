class MyHashMap:

    def __init__(self):
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        if key not in self.dict.keys():
            self.dict.__setitem__(key, value)
        else:
            self.dict[key] = value

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.dict.keys():
            return self.dict.pop(key)


# Your MyHashMap object will be instantiated and called as such:
key = 4
value = 6
obj = MyHashMap()
obj.put(key, value)
param_2 = obj.get(key)
obj.remove(key)

