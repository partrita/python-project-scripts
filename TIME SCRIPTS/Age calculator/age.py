from datetime import date

name = input("What is your name: ")

Birth_Year = int(input("Enter your birth year: "))

Current_year = date.today().year

def age_caluu():
    Age_calculated = (Current_year - Birth_Year)
    print (f'Hey {name} your age is {Age_calculated}')
age_caluu()
