def fizzBuzz(n: int) -> list[str]:
    l=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            l.append("FizzBuzz")
        elif i%3==0:
            l.append("Fizz")
        elif i%5==0:
            l.append("Buzz")
        else:
            l.append(str(i))
    print(l)


n = 15
# Output: ["1","2","Fizz"]
fizzBuzz(n)