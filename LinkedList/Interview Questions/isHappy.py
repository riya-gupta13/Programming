# def square(n):
#     ans = 0
#     while n > 0:
#         rem = n % 10
#         ans += rem * rem
#         n = n / 10
#     return ans
#
#
# def isHappy(n: int) -> bool:
#     slow = n
#     fast = n
#     while True:
#         slow = square(slow)
#         fast = square(square(fast))
#         if not (slow != fast):
#             break
#     if slow == 1:
#         return True
#     return False
#
#
# print(isHappy(2))


def gen(self, n: int) -> int:
    # Convert n to a list of digits and then sum the square of those digits
    return sum(map(lambda x: int(x) ** 2, str(n)))


def isHappy(self, n: int) -> bool:
    # Initialise the slow and fast pointer to be head and head.next
    slow, fast = n, self.gen(n)
    # While we have not detected a cycle and the fast pointer has not converged to 1
    while fast != slow and fast != 1:
        # Increment the slow and fast pointers
        slow, fast = self.gen(slow), self.gen(self.gen(fast))
    # Return whether fast converged to 1 (otherwise return the fact that a cycle was detected)
    return fast == 1