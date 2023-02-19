def minMovesToSeat(seats: list[int], students: list[int]) -> int:
    sum = 0
    seats = sorted(seats)
    students = sorted(students)
    for i in range(0, len(seats)):
        sum = sum + abs(seats[i] - students[i])
    print(sum)


seats = [45, 36, 83, 35, 90, 54, 66, 13, 57, 87, 22, 36, 16, 39, 29, 70, 58, 20, 32, 13, 67, 80, 1, 83, 42, 53, 12, 81,
         24, 27, 100, 24, 54, 82, 76, 88]
students = [57, 17, 63, 10, 27, 95, 59, 27, 67, 4, 90, 27, 29, 46, 20, 88, 55, 62, 54, 83, 66, 33, 61, 15, 53, 45, 23,
            25, 91, 72, 14, 45, 61, 29, 13, 63]
# Output: 148
minMovesToSeat(seats, students)
