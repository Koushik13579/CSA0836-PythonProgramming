date=input("Enter date as dd/mm/yyyy:")
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_anniversary(date):
    day, month, year = map(int, date.split('/'))
    if is_leap_year(year):
        return f"Leap Year. Anniversary Date: {day:02d}/{month:02d}/{year + 1}"
    else:
        return f"Non Leap Year. Anniversary Date: {day:02d}/{month:02d}/{year - 1}"
print("Given Anniversary Year:",calculate_anniversary(date))
