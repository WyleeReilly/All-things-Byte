"""
create a program file that takes two functions:
age_to_time - should take the persons are in years and return it in months, days, and horus.
birthday_to_time - 
"""

from datetime import datetime
from datetime import date


#This is the converter of age in years to months, days, and hours
def age_to_time():
    age = input("What is the age you would like to convert?\n> ")
    month_age = age * 12
    day_age = age * 360
    hour_age = age * 8640
    minutes_age = age * 21600
    conversion = f"months: {month_age}, days: {day_age} , hours: {hour_age}, minutes: {minutes_age} "
    print(conversion)


#This is the converter of birthday to age
def birthday_to_time():
    birthday = input("Please enter the birthday in 'MM-DD-YYYY' Format\n> ")
    #First stripping the input and converting to date format
    birthday_in_date_type = datetime.strptime(birthday, "%m-%d-%Y").date()
    #Then creating a time for today
    today_in_date_type = date.today()
    #Subtracting TODAY minus the BIRTHDAY given
    age = str(today_in_date_type - birthday_in_date_type)
    #Needed to cut the conversion of age because it returns '9090 days 00:00...
    #..and I couldn't get this time-delta data type to drop the zeros
    age_in_days = int(age[:4])
    #Then went about basic arithmetic
    age_in_months = age_in_days / 12
    age_in_hours = age_in_days *24
    age_in_minutes = age_in_hours *60
    #final output
    conversion = f"months: {age_in_months}, days: {age_in_days}, hours: {age_in_hours}, minutes: {age_in_minutes} "
    print(conversion)



#This is the engine
def birthday():
    print("Are you providing an age, or a birthday?")
    response = input("> ")
    if response == "age":
        age_to_time()
    elif response == "birthday":
        birthday_to_time()
    else: 
        print("Oh- you're one of those people who don't listen to directions. cool.")

birthday()
#print(birthday_to_time("03-22-1995"))
