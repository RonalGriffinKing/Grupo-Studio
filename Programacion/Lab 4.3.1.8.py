def is_year_leap(year):
    if year % 4 != 0: #no divisible entre 4
            return False
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
            return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
            return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
            return True

def days_in_month(year, month):

    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def day_of_year(year, month, day):
     
    days = 0
    for m in range(1, month):
        days += days_in_month(year, m)
    return days + day
    
    
print(day_of_year(2001, 5, 31))
