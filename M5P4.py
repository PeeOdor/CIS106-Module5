# Computes an appliance's warranty cost and total price based on its cost tier.
name = input("Enter appliance name: ")
cost = float(input("Enter appliance cost: "))
 
if cost > 1000:
    warranty = cost * 0.10
else:
    warranty = cost * 0.05
 
total = cost + warranty
 
print("Name:", name)
print("Cost: $%.2f" % cost)
print("Warranty: $%.2f" % warranty)
print("Total: $%.2f" % total)
 