# Determines unit price and extended price for an item based on its code (A or B).
item = input("Enter item (A or B): ")
quantity = int(input("Enter quantity: "))
 
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00
 
extended_price = quantity * unit_price
 
print("Item:", item)
print("Unit Price: $%.2f" % unit_price)
print("Extended Price: $%.2f" % extended_price)
 