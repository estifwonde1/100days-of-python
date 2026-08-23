print("let's print the day in a month")
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
                return "leap_year"
            else:
                print("not a leap year")
                return "not_leap_year"
        else:
            print("leap year")
            return "leap_year"
    else:
        print("not a leap year")
        return "not_leap_year"
def days_in_month(year , month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    indie = month - 1   
    if is_leap(year) == "leap_year":
        month_days[1] = 29
        return month_days[indie]
    return month_days[indie]
year = int(input("please enter the year"))
month = int(input("enter the month as a number")) 


print(days_in_month(year,month)) 

