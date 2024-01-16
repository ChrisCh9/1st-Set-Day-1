#Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay. 

total_bill_price = float(input("How much was the total bill price? "))

amount_of_diners = int(input("How many diners are there? "))

amount_per_person = float(total_bill_price / amount_of_diners)

print("Every person should pay", amount_per_person)