import math


def checkPerfectNumber(num: int) -> bool:
    if num == 1:
        return False

    def sum_of_divisors(num):
        divisors = [1]
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num / i:
                    divisors.append(num / i)
        return divisors

    return sum(sum_of_divisors(num)) == num


print(checkPerfectNumber(6))
