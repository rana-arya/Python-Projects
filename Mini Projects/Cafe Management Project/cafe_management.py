# Cafe Management System
# Author: Arya Rana
# Language: Python

menu = {}

menu["coffee"] = {"price": 50, "category": "Drink"}
menu["masala chai"] = {"price": 40, "category": "Drink"}
menu["green tea"] = {"price": 45, "category": "Drink"}
menu["black tea"] = {"price": 35, "category": "Drink"}
menu["ginger tea"] = {"price": 50, "category": "Drink"}
menu["samosa"] = {"price": 20, "category": "Snack"}
menu["sandwich"] = {"price": 60, "category": "Snack"}
menu["muffin"] = {"price": 30, "category": "Snack"}
menu["pastry"] = {"price": 50, "category": "Snack"}

print("Welcome to Bhaichara Café!")
print("Here's our menu for today:")

print("\nDrinks:")
for name, details in menu.items():
    if details["category"] == "Drink":
        print(name.title() + ". Rs. " + str(details["price"]))

print("\nSnacks:")
for name, details in menu.items():
    if details["category"] == "Snack":
        print(name.title() + ". Rs. " + str(details["price"]))

orders = []
order_history = []

while True:
    name = input("\nEnter your name: ").strip()
    contact_number = input("Enter your 5-digit contact number: ").strip()
    while len(contact_number) != 5 or not contact_number.isdigit():
        contact_number = input("Invalid contact number! Please enter a 5-digit contact number: ").strip()
    
    while True:
        item = input("\nEnter the item you want to order (or type 'done' to finish): ").strip().lower()
        if item == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        
        if item in menu:
            order_total = menu[item]["price"] * quantity
            orders.append((item, quantity, order_total))
            print("You've ordered " + str(quantity) + " x " + item.title() + " for Rs. " + str(order_total))
        else:
            print("Sorry, " + item.title() + " is not found in the menu. Please choose another item.")
        
        more = input("Would you like to order anything else, Sir/Madam? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    
    order_details = {
        "name": name,
        "contact_number": contact_number,
        "orders": orders.copy(),
        "subtotal": sum(order[2] for order in orders)
    }
    order_history.append(order_details)
    orders.clear()
    
    print("\nThank you for your order, " + name + "!")
    print("Your subtotal is: Rs. " + str(order_details["subtotal"]))
    print("Please proceed to the counter for payment. Have a great day!")
    
    another_customer = input("\nIs there another customer waiting to order? (yes/no): ").strip().lower()
    if another_customer != 'yes':
        break

print("\nOrder History:")
customer_number = 1
for record in order_history:
    print("\nCustomer " + str(customer_number) + ":")
    print("Name: " + record['name'])
    print("Contact Number: " + record['contact_number'])
    print("Orders:")
    for order in record["orders"]:
        print(" -> " + str(order[1]) + " x " + order[0].title() + " (Total: Rs. " + str(order[2]) + ")")
    print("Subtotal: Rs. " + str(record['subtotal']))
    customer_number += 1






