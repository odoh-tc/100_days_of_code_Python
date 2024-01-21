def is_leap(t_year):
    if t_year % 4 == 0:
        if t_year % 100 == 0:
            if t_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(t_year, t_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    calender = ["January", "February", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]
    m_cal = calender[t_month - 1]
    if t_month == 2 and is_leap(t_year):
        return m_cal, 29
    else:
        return m_cal, month_days[t_month - 1]


year = int(input("Which year do you want to check?: \n"))
month = int(input("Which month do you want to check?: \n"))
m_cal, days = days_in_month(year, month)
print(f"The number of days in {m_cal} of the year {year} is {days}days.")
