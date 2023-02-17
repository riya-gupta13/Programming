# PRINT LEAP YEARs BETWEEN 2000 AND 2050
import re

start = 2000
end = 2050
# count = 0
# while start != end:
#     if start < end:
#         if start % 4 == 0 and start % 100 != 0:
#             print(start)
#         if start % 100 == 0 and start % 400 == 0:
#             print(start)
#     start += 1

# FINDING DUPLICATE NUMBERS with frequency IN GIVEN ARRAY
arr = [6, 1, 2, 7, 1, 9, 1, 0, 4, 0, 2, 5]
# Output:
# 
# 1 is repeated 3 times
# 2 is repeated 2 times
# 0 is repeated 2 times
d = {}
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
for i in d:
    if d[i] > 1:
        s = "{} is repeated {} times".format(i, d[i])
        print(s)

String = "My number is 415-555-4242."
pattern = "\d{3}[-]\d{3}[-]\d{4}"
l = re.findall(pattern, String)
s=re.search("\d{3}-", String)

print(l,s.group(0).replace('-',''),re.split('-',l[0]))
