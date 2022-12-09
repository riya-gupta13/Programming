def reformatDate(date: str) -> str:

    dates = date.split(' ')
    print(dates)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    m = months.index(dates[1]) + 1
    print(m)
    if len(str(m)) != 2:
        month = '0' + str(m)
    else:
        month = str(m)
    num = dates[0]
    d = num[0:2]
    # finalD = ''
    if not d.isdigit():
        finalD = '0' + d[0]
    else:
        finalD = d
    print(finalD)
    new = dates[2] + '-' + month + '-' + finalD
    print(new)


date = "6th Jun 1933"
# Output: "2052-10-20"
reformatDate(date)
