# The key observation here is that it's free to move a chip from an even number to another even number,
# and it is free to move a chip from an odd number to another odd number. It only costs to move an even to an odd,
# or an odd to an even. Therefore, we want to minimise such moves.
#
# All chips must be on the same position once we're done, which is either even or odd. Therefore, we want to
# calculate whether it is cheaper to move all the odd chips to even or all the even chips to odd. This will simply
# come down to how many even chips we start with, and how many odd chips. Each chip that has to be moved will cost
# exactly 1.
def minCostToMoveChips(self, position: list[int]) -> int:
    even_parity = 0
    odd_parity = 0
    for chip in position:
        if chip % 2 == 0:
            even_parity += 1
        else:
            odd_parity += 1
    return min(even_parity, odd_parity)


# position = [1,2,3]
# Output: 1