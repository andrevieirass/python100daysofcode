"""
# INSTRUCTIONS #
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

Example Input
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7

Example Output
Each person should pay: $19.93
"""
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# tip_percent = tip / 100
# total_tip = bill * tip_percent
# total_bill = bill + total_tip
# bill_per_person = total_bill / people
# # final_amount = round(bill_per_person, 2)
# # final_amount = "{:.2f}".format(bill_per_person)
# final_amount = f"{bill_per_person:.2f}"

tip_percent = 1 + (tip / 100)
total_bill = bill * tip_percent
bill_per_person = total_bill / people
final_amount = f"{bill_per_person:.2f}"

print(f'Each person should pay: ${final_amount}')
