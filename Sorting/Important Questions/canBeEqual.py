def canBeEqual(target: list[int], arr: list[int]) -> bool:
    if sorted(target)==sorted(arr):
        print("True")
    else:
        print("False")



target = [3,7,9]
arr= [3,7,11]
# Output: true
canBeEqual(target,arr)


