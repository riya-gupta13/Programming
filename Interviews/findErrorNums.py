# turing test
def findErrorNums(nums):
    result = []
    for i in range(0, len(nums)):
        correct = i + 1
        # print(correct)
        if nums[i] != correct:
            result.append(nums[i])
            result.append(correct)

    print(result)


nums = [1, 2, 2]
findErrorNums(nums)
