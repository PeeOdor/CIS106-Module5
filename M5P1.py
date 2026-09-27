# Calculates extended price, tax, and total cost based on quantity-based unit pricing.
quantity = int(input("Enter quantity: "))
 
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00
 
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax
 
print("Quantity:", quantity)
print("Unit Price: $%.2f" % unit_price)
print("Extended Price: $%.2f" % extended_price)
print("Tax: $%.2f" % tax)
print("Total: $%.2f" % total)
 