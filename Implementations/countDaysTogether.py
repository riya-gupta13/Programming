def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    months = [0] + [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    arriveAlice = arriveAlice.split('-')
    leaveAlice = leaveAlice.split('-')
    arriveBob = arriveBob.split('-')
    leaveBob = leaveBob.split('-')

    arriveAlice = sum(months[:int(arriveAlice[0])]) + int(arriveAlice[1])
    leaveAlice = sum(months[:int(leaveAlice[0])]) + int(leaveAlice[1])
    arriveBob = sum(months[:int(arriveBob[0])]) + int(arriveBob[1])
    leaveBob = sum(months[:int(leaveBob[0])]) + int(leaveBob[1])

    arrive = max(arriveAlice, arriveBob)
    leave = min(leaveAlice, leaveBob)

    return max(leave - arrive + 1, 0)


arriveAlice = "08-15"
leaveAlice = "08-15"
arriveBob = "08-16"
leaveBob = "08-19"
print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
