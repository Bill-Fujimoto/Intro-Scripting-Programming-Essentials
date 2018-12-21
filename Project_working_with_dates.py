''' Working with dates '''

import datetime

def days_in_month(year, month):
    ''' computes the number of days in a given month'''
    
    if month == 12:
        month_ = 1
        year_ = year + 1
    else:
        month_ = month + 1
        year_ = year
    
    num_days = datetime.date(year_, month_, 1) - datetime.date(year, month, 1)
    return num_days.days


def is_valid_date(year, month, day):
    ''' checks for valid date, returns True if valid, False otherwise '''
 
    try:
        datetime.date(year, month, day)
    except:
        return False
        
    return True
    
def days_between(year1, month1, day1, year2, month2, day2):
    ''' checks for the number of days between two valid dates, returns 0 if delta < 0
    The parameters with suffix 2 is the later date'''
    
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        delta = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
        if delta.days >= 0:
            return delta.days
        else:
            return 0
    else:
        return 0

def age_in_days(year, month, day):
    ''' calculates the age in days from date of birth, returns 0 if age < 0'''
    
    age = days_between(year, month, day, datetime.date.today().year,\
        datetime.date.today().month, datetime.date.today().day)
    return age
    
print(age_in_days(1958, 5, 3))    
print ()
print(days_in_month(2020, 2))
