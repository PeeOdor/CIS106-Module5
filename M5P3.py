# Calculates a book order total and applies free shipping over $50, otherwise a $25 charge.
num_books = int(input("Enter number of books: "))
cost_per_book = float(input("Enter cost per book: "))
 
order_total = num_books * cost_per_book
 
if order_total > 50.00:
    shipping = 0
else:
    shipping = 25.00
 
print("Order Total: $%.2f" % order_total)
print("Shipping: $%.2f" % shipping)
 