def average(salary: list[int]) -> float:
    s=sorted(salary)
    l=s[1:len(s)-1]
    avg=sum(l)/len(l)
    print(avg)


salary = [1000,2000,3000]
# Output: 2500.00000
average(salary)