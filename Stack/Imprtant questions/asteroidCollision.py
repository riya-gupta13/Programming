def asteroidCollision(self, asteroids: list[int]):
    stack = []
    for i in asteroids:
        # here we are chkng this i<0 and stack>0 as only the collision will hppn if thy are in opp direction
        while stack and i < 0 and stack[-1] > 0:
            # as if diff is negative it means stack elemnt needs to remove else set i=0 as they have given i cnnt be 0
            # so with that we can use i later to appnd or not in stack
            diff = i + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                i = 0
            else:
                i = 0
                stack.pop()
        if i:
            stack.append(i)
    return stack
