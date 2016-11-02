# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:34:12 2016

@author: srowe
"""

month_names = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
def days_in_month(month, year):
    days_per_month = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 1:
        return days_per_month[month]
        
    if year % 4 == 0:
        if year % 100 > 0 or year % 400 == 0:
            # Leap year
            return 29
            
    return 28
    
def days_in_year(year):
    d = 0;
    for m in range(12):
        d += days_in_month(m, year)
    return d
    
#
# Day 0 is Jan 1, 1900 and it is a Monday.  Therefore, any day
# that is divisible evenly by 7 is a Monday.  But we are looking
# for Sundays, which are day % 7 == 6.
if __name__ == '__main__':
    day = days_in_year(1900)
    sundays_on_first = 0
    for year in range(1901, 2001):
        for month in range(12):
#            print 'testing ', month_names[month], year
            if day % 7 == 6:
                # Sunday, Sunday, Sunday!
                sundays_on_first += 1
                print sundays_on_first, year, month_names[month]
            day += days_in_month(month, year)
        
    print sundays_on_first