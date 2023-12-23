print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))
percentage_tip = 1 + int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))

per_person_bill = (total_bill / people) * percentage_tip
print(f"Each person should pay: {per_person_bill:.2f}")
