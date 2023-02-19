import datetime


def calculate_age(born):
    today = datetime.datetime.today()
    # In this example, the current date is July 1st and the birth date is December 31st. The difference in years is
    # today.year - born.year = 2021 - 1997 = 24. The comparison (7, 1) < (12, 31) returns True, so the final result
    # is 24 - True = 23. This means that the person is 23 years old and has not yet had their birthday this year.
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# Test the function
birthday = datetime.datetime(1997, 12, 12)
age_in_days = calculate_age(birthday) * 365
print(f"Age in days: {age_in_days}")
