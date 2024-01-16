#Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.

num_over_100 = int(input("Please enter a number over 100: "))

num_under_10 = int(input("Please enter a number under 10: "))

#times_smaller_fit_in_larger = num_over_100 / num_under_10 #Float answer
times_smaller_fit_in_larger = int(num_over_100 / num_under_10) #Int answer 

print("The smaller fit ", times_smaller_fit_in_larger, " times in the larger one") 