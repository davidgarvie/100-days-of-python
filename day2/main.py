print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? ")
)
number_of_people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + (tip_percentage / 100))
amount_per_person = round(bill_with_tip / number_of_people, 2)
formatted_amount = format(amount_per_person, ".2f")
print(f"Each person should pay: ${formatted_amount}")
