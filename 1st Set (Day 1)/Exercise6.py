#Ask how many slices of pizza the user started with and ask how many slices they have eaten.Work out how many slices they have left and display the answer in a user friendly format. 

starting_pizza_slices = int(input("Please enter how many slices have you stared: "))

eated_pizza_slices = int(input("Please enter how many slices have you eated: "))

left_pizza_slices = starting_pizza_slices - eated_pizza_slices

print("The slices of pizza that have been left are: " ,left_pizza_slices)