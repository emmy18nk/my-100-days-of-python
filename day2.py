#Age & Life Timeline Calculator

name = input("Enter your name? ")

age = int(input("Enter your age please? "))

birth_year = 2026 - age 

months_alive = age * 12

weeks_alive = months_alive * 4

days_alive = weeks_alive * 7

hours_alive = days_alive * 24

minutes_alive = hours_alive * 60

seconds_alive = minutes_alive * 60

age_in = int(input("enter any number you would like to see your age then? "))
future_age = age_in + age

print(f"{name}, you have been alive since {birth_year}" 
f" for approximately {age} years,{months_alive} months,"
f"{weeks_alive} weeks,{days_alive} days.")

print(future_age)