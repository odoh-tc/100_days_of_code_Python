print("Welcome to the Tip Calculator.")

bill = float(input("What was the total bill?\n"))

tip = float(input("How many tip would you like to give? 10, 12, or 15\n"))

people = float(input("How many people to split the bill?\n"))

bill_with_tip = bill * (1 + tip / 100)

bill_per_peron = bill_with_tip / people
bill_round_figure = round(bill_per_peron)
print(f"Each person should pay ${bill_round_figure}")

