menu = {
    'Pizza': 40,
    'Pasta': 80,
    'Burger': 80,
    'Tea': 50,
    'Coffee': 70,
    'pizza': 40,
    'pasta': 80,
    'burger': 80,
    'tea': 50,
    'coffee': 70,
    'PIZZA': 40,
    'PASTA': 80,
    'BURGER': 80,
    'TEA': 50,
    'COFFEE': 70,
}

print("Welcome To Friday Restaurant")
print(" Pizza  : Rs40\n Pasta  : Rs80\n Burger : Rs80\n Tea    : Rs50\n Coffee  : Rs70\n")

order_total = 0

item_1 = input("Enter the name of the first item you want to order: ").strip()  # Use strip to remove any extra whitespace

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No): ")

if another_order.lower() == "yes":  # Use .lower() to handle variations in case
    item_2 = input("Enter the name of the second item: ").strip()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount to pay is {order_total}")
