import datetime


def daysBetweenDates(date1: str, date2: str) -> int:
    f1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
    f2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
    left = f2 - f1
    print(left.days)
    print(f1)


date1 = "2020-01-15"
date2 = "2019-12-31"
daysBetweenDates(date1, date2)
