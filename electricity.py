unit = int(input("Please enter the number of units you have consumed: "))
amount = 0
tax = 0
if unit<=50:
    amount = unit * 3 
    tax = 30 
elif unit<=100:
    amount = 150 + ((unit - 50) * 5)
    tax = 50
elif unit<=200:
    amount = 150 + 250 + ((unit - 100) * 6)
    tax = 100 
else:
    amount = 150 + 250 + 600 + ((unit - 200) * 7)
    tax = 150 
total_amount = amount + tax
print("Your tax bill is summed upto", total_amount)
