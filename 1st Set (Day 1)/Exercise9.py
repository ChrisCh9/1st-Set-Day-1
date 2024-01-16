#Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.

num_of_days = int(input("Please enter the number of days you want to be analytically calculated in hours, minutes and seconds: "))

hours_of_days = num_of_days * 24

minutes_of_days = hours_of_days * 60

seconds_of_days = minutes_of_days * 60

print("In", num_of_days, "days", "there are", hours_of_days , "hours or", minutes_of_days, "minutes or", seconds_of_days, "seconds")