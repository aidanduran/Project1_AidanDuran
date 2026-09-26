shopper_name = "aIDAN duRAn"
grocery_1_cost = 2.58
grocery_2_cost = 4.25
grocery_3_cost = 3.34
grocery_4_cost = 7.30
grocery_5_cost = 5.59
grocery_1_amount = 3
grocery_2_amount = 3
grocery_3_amount = 4
grocery_4_amount = 1
grocery_5_amount = 2

print(f"{shopper_name.title()}'s grocery costs:")
print(f"Total grocery cost: ${round((grocery_1_cost * grocery_1_amount) + (grocery_2_cost * grocery_2_amount) + (grocery_3_cost * grocery_3_amount) + (grocery_4_cost * grocery_4_amount) + (grocery_5_cost * grocery_5_amount), 2)}")
