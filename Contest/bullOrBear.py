number=int(input())
x,y = input().split()
while number!=0:
    if int(x)>int(y):
        print("LOSS")
    elif int(x)<int(y):
        print("PROFIT")
    else:
        print("NEUTRAL")
    number-=1

# Practicing mcq questions
import math
import queue
import threading
import time
from collections import Counter


#
# #
# def solution():
#     a, c = input().split()
#     a = int(a)
#     c = int(c)
#     b = (c + a) / 2
#     print(b)
#     if abs(b) == b:
#         print(b)
#     else:
#         print(-1)
#
#
# t = int(input())
# while (t > 0):
#     t = t - 1
#     solution()

def sum():
    print(tuple(zip([1, 2], [1, 2, 3])))


sum()


class Evens:
    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        return x


my = Evens()
i = iter(my)
next(i)
next(i)
next(i)
print(next(i))
d = "abc".join("def")
print(d)
l = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
d = dict(zip(l, l2))
print(d.get(5))
days = ['m', 't', 'w', 'th']
c = Counter(days)
for x in range(1, 5, 2):
    d = x % 3
    c.update([days[d]] * x)
print(c)
print(complex(2))
print(2j)

sum = 0
i = 10
while i < 1:
    sum += i
    sum = sum * 2
    i -= 1
print(sum)
x = ["1", "2", "-7", "15", "300"]
print(sorted(x))


def fun(arr):
    temp = 0
    for x in arr:
        if x % 2 == 1:
            temp += 1
        else:
            temp = 0
        if temp == 3:
            return True
    return False


print(fun([4, 5, 7, 23, 12]))


def root(se):
    r = {}
    for s in se:
        base = r
        for word in s.split(' '):
            if not base.get(word):
                base[word] = {}
            base = base[word]
    return r


print(root(["hello world", "hello there"]))
print(math.floor(-2))
print(round(-2))
print(math.ceil(2))
print(abs(math.floor(-5.1)))


def dele(items):
    i = 0
    while i < len(items):
        if len(items[i]) == 0:
            del items[i]
        i += 1


names = ['Rachel', '', 'Meghna', '', '', 'Tim']
dele(names)
print(names)
q = queue.Queue()
for i in [3, 2, 1]:
    def f():
        time.sleep(i)
        q.put(i)


    threading.Thread(target=f).start()
print(q.get())


def has(nums):
    pos = False
    neg = False
    for num in nums:
        pos = num > 0
        neg = num < 0
    print(pos, neg)
has([0,-1,-2])
sorted(sorted(["riya",'murali',"22/2/13","22/8/28"], key=lambda o: o.date, reverse=True), key=lambda o: o.name)
