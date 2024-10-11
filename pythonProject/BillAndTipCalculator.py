#prints header
print("Welcome to Ashley's Tip Calculator!\n")
#takes in input of total bill, converts it to a float date type and stores it in the variable TotalBill
TotalBill = float(input("How much is the total bill please?\n"))
#takes in input of tip wanted to give, converts it to a float date type and stores it in the variable Tip
Tip = float(input("How much tip would you like to give? 10, 15 0r 20?\n"))
#takes in input of total amount of people paying, converts it to a float date type and stores it in the variable
# TotalPeople
TotalPeople = float(input("How many people are sharing the bill?\n"))
#each variable below stores the percentage tip
amount1 = 10 / 100
amount2 = 15 / 100
amount3 = 20 / 100
#the total bill of each person is calculated by adding the percentage bill to the total and dividing amongst the total
#number of people paying and then rounding it to the next two decimal places and storing in respected variables
Sum1 = round((TotalBill + (TotalBill * amount1)) / TotalPeople, 2)
Sum2 = round((TotalBill + (TotalBill * amount2)) / TotalPeople, 2)
Sum3 = round((TotalBill + (TotalBill * amount3)) / TotalPeople, 2)
#the if/else statement for each condition is introduced to run on expected input
if Tip == 10:
    print(f"Each person's bill is {Sum1}")
elif Tip == 15:
    print(f"Each person's bill is {Sum2}")
elif Tip == 20:
    print(f"Each person's bill is £{Sum3}")
else:
    print("PLEASE INPUT DETAILS REQUIRED!")
