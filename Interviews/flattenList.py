l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], ([4], 5), 'name']


# output: [1, 'a', 'cat', 2, 3, 'dog', 4, 5, 'name']


def flatten_list(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


flattened_list = flatten_list(l)
print(flattened_list)

# map keys to keys
dict1 = {"place": "India", "location": "Pune", "name": "Riya"}
dict2 = {"Usa": "place", "Chicago": "location", "akash": "name"}
# output: {'place': 'Usa', 'location': 'Chicago', 'name': 'akash'}

print(dict(zip(dict1.keys(), dict2.keys())))
# print([ key1,value1,key2,value2 for key1,value1 in dict1.items() for key2,value2 in dict2.items())])
# print(dict1.keys())

# lambda fxn to find odd
findodd = lambda x: x % 2 != 0
odd = filter(findodd, range(1, 21))
print(list(odd))
print(list(filter(lambda x: x % 2 != 0, range(1, 21))))
