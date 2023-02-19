def find132pattern(nums: list[int]) -> bool:
    # approach-- we are using stack that is monotonically decreasing frst we will be trying to find element k,
    # for that wht will we do is we will append in stack only if the element less than element present in stack
    # otherwise pop until its greater and with this at every point we will also have a min element tht is min to the
    # left of num, so tht ltr we can find j and if min is less thn tht return True

    stack = []  # pair [num,minLeft] mono decreasing
    curMin = nums[0]
    for n in nums[1:]:
        while stack and n >= stack[-1][0]:
            stack.pop()
        # after popping still elmnts there in stack, chk min
        if stack and n > stack[-1][1]:
            return True
        stack.append([n, curMin])
        curMin = min(curMin, n)
    return False




